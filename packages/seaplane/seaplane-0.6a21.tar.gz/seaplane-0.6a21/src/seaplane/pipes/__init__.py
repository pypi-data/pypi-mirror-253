import os
from typing import Any, Callable, Dict, List, Optional, Set, Union
from seaplane.pipes.status import status
from seaplane.config import config
from seaplane.errors import SeaplaneError

from seaplane.sdk_internal_utils.buckets import create_bucket_if_needed

from .executor import execute


"""
Deploy your applications to the Seaplane platform by using
Apps, Dags, and Flows.

# An App is a unit of deployment on Seaplane.
# Use an app to connect units of work together,
# and associate your application with Seaplane
# resources like HTTP endpoints and object store buckets.

app = seaplane.pipes.App("my-app")

# The work of apps is composed of Dags. Dags (Directed Acyclic Graphs)
# are collections of connections between the working python
# functions in your application. You can create an Dag using
# an application.

dag = app.dag("my-dag")

# You can use a dag to build Flows, which map to running
# processes on Seaplane infrastructure. To create a
# Flow, you need a dag, and some input sources, and a python
# function that does the work of the Flow.

def emphasize(context):
    yield context.body + b'!'

def intensify(context):
    yield context.body + 'b' for real'

# The first argument to dag.task is the function, the second is the input.

intensify_task = dag.task(intensify, [app.input()])
emphasize_task = dag.task(emphasize, [intensify_task])

# to associate an output with a dag, call `dag.respond()`

dag.respond(emphasize_task)

# to associate the output of a Flow or Dag with an App, do the same thing

app.respond(dag) # you can also write `app.respond(emphasize_task)` here

# Calling app.start() will deploy an application from your workstation,
# and *run* that application on the Seaplane platform.
app.start()
"""


class Subject:
    """
    Subject is a pubsub subject. Flows publish messages associated with
    a subject to communicate with the outside world.

    Subject should represent a concrete, publishable subject - it can
    contain fun ${! meta} macros, but should not contain wildcards.

    Flows can write to subjects but not subscribe to them.

    app.edge(my_task, Subject("known-stream.explicit-subject"))
    """

    def __init__(self, subject: str):
        self.subject = subject

    def __hash__(self) -> int:
        return hash(self.subject)

    def __eq__(self, other: Any) -> Any:
        return self.subject == other.subject


class Subscription:
    """
    The possibly-filtered name of a subject, for matching. Flows listen
    to subscriptions for their inputs.

    Should not ever contain macros and things, but may contain wildcards.

    Tasks can subscribe to Subscriptions but not write to them.

    app.edge(Subscription("known-stream.explicit-subscription.>"), my_task)
    """

    def __init__(self, filter: str, deliver: str = "all"):
        self.filter = filter
        self.deliver = deliver

    def __hash__(self) -> int:
        return hash(self.filter)

    def __eq__(self, other: Any) -> Any:
        return self.filter == other.filter

    def stream(self) -> str:
        return self.filter.split(".", 1)[0]


class _FlowSubject(Subject):
    """Flow subjects conform to a standard format

    app.task.address-tag.output_id.batch.batch.batch

    Because of this, they can be converted into subscriptions for peers.
    """

    def __init__(self, app_name: str, instance_name: str):
        self.app_name = app_name
        self.instance_name = instance_name
        super(_FlowSubject, self).__init__(
            f"{app_name}.{instance_name}"
            '.${! meta("_seaplane_address_tag") }'
            '.${! meta("_seaplane_output_id") }'
            '${! meta("_seaplane_batch_hierarchy") }'
        )

    def flow_subscription(self, address: str) -> Subscription:
        """use address = '*' to match all outputs from this task"""
        return Subscription(f"{self.app_name}.{self.instance_name}.{address}.>")


class Flow:
    """
    Description of deployment intent associated with a Seaplane flow.

    Create flows through an Dag, like this

    app = App("app")

    dag = app.dag("task-demo")

    def do_it(context: Messsage) -> Result:
        yield Result(b"Hello, " + context.body)

    my_task = dag.flow(do_it)

    Flow functions will be passed a Seaplane message, and
    should yield a Seaplane result. For convenience,
    if a task returns bytes (or something that can be converted
    into bytes), that value will be converted to bytes
    and packaged into a Result automatically.

    Once created, Flows can be wired together with other flows,
    application resources, or other Dags with `dag.edge`

    dag.edge(app.input(), my_task)
    dag.edge(my_task, app.output())
    """

    def __init__(
        self,
        dag: "Dag",
        work: Callable[..., Any],
        instance_name: str,
        subject: _FlowSubject,
        replicas: int,
        ack_wait_secs: int,
    ):
        # Note that app is a circular reference, so Tasks will not be GC'd
        self.dag = dag
        self.work = work
        self.instance_name = instance_name
        self.subject: Subject = subject  # task output
        self.replicas = replicas
        self.ack_wait_secs = ack_wait_secs
        self.subscriptions: Set[Subscription] = set()  # pull input from these subjects

    def subscribe(self, source: Subscription) -> None:
        self.subscriptions.add(source)


EdgeFrom = Union[Flow, "Dag", Subscription, "Bucket"]
EdgeTo = Union[Flow, Subject]


# For historical reasons, we need to be sure that
# these defaults work the same both for Dag.flow() and Dag.task()
_DEFAULT_REPLICAS = 1
_DEFAULT_ACK_WAIT_SECS = 2 * 60


class Dag:
    """
    Dag is a namespace and unit of deployment for
    a collection of Tasks. Dags create a namespace for task messages
    and manage deployment together.

    Create Dags through an application, like this

    app = App("my-app")
    dag = app.dag("my-dag")

    Dags are a namespace for their associated flows, so while the names
    of flows must be unique per dag, you can use the same flow name
    in different Dags. You can communicate between Dags either by
    wiring their flows together directly, or by calling `dag.respond()`
    with a flow that represents the single output of the dag (if that
    makes sense for your application)

    dag1 = app.dag("dag-1")
    dag2 = app.dag("dag-2")

    t1 = dag1.task(work1, [app.input()])
    dag1.respond(t1)

    # It's ok to connect tasks across Dag boundaries
    t2 = dag2.task(work2, [t1])

    # since we've configured dag1 to respond with t1's output, this works just the same
    # as the line above
    t2 = dag2.task(work2, [dag1])
    """

    def __init__(self, name: str):
        """use App.dag to create Dags"""
        self.name = name
        self.flow_registry: Dict[str, Flow] = {}
        self.response: Optional[Flow] = None

    def task(
        self,
        work: Callable[..., Any],
        sources: List[EdgeFrom],
        instance_name: Optional[str] = None,
        replicas: int = _DEFAULT_REPLICAS,
        ack_wait_secs: int = _DEFAULT_ACK_WAIT_SECS,
    ) -> Flow:
        """
        Dag.task() is a convenience method for describing a new flow, along
        with its inputs.

        Dag.task() returns a reference to the created flow, that can be used
        to subscribe subsequent flows to the created flow's output.
        """
        ret = self.flow(
            work, instance_name=instance_name, replicas=replicas, ack_wait_secs=ack_wait_secs
        )
        for source in sources:
            self.edge(source, ret)

        return ret

    def respond(self, tail: Union["Dag", Flow]) -> None:
        """
        Dag.respond() is a convenience for wiring tasks to
        the output of the dag.

        While you can wire flows together directly across dag boundaries,
        for many dags (that have a single, interesting output) it can
        be convenient to treat the dag itself as the source of messages.
        To do this, call `Dag.respond()` with the interesting output
        flow as an argument.

        Dags that have a response configured can be used as sources for
        other Flows.
        """
        if isinstance(tail, Dag):
            if tail.response is None:
                raise SeaplaneError(
                    f"{tail.name} has no response. Call Dag.respond on it, "
                    "or connect directly to it's tasks"
                )
            self.respond(tail.response)
        else:
            self.response = tail

    def flow(
        self,
        work: Callable[..., Any],
        instance_name: Optional[str] = None,
        replicas: int = _DEFAULT_REPLICAS,
        ack_wait_secs: int = _DEFAULT_ACK_WAIT_SECS,
    ) -> Flow:
        """
        Use Dag.flow to create an unwired flow, that can be associated
        with other flows by calling dag.edge().
        """
        if instance_name is None:
            instance_name = work.__name__.replace("_", "-") + "-default"

        prefixed_name = self.name + "-" + instance_name

        if prefixed_name in self.flow_registry:
            raise SeaplaneError(
                f"duplicate task name {prefixed_name} in dag {self.name}."
                " Try providing a unique instance_name argument when you create your task"
            )

        subject = _FlowSubject(self.name, prefixed_name)
        ret = Flow(self, work, prefixed_name, subject, replicas, ack_wait_secs)
        self.flow_registry[ret.instance_name] = ret
        return ret

    def edge(
        self,
        source: EdgeFrom,
        dest: EdgeTo,
    ) -> None:
        """
        Add an edge from a to b, binding b to a's output.

        Flows can be wired to publish information to other tasks and explicit subjects.
        Flows can be wired to recieve information from other tasks or subscriptions.

        If source is not a Flow or a Dag that responds with a task, then dest must be a Flow.
        """
        if isinstance(source, Dag):
            if source.response is None:
                raise SeaplaneError("Call Dag.response(..), or compose individual tasks together.")

            return self.edge(source.response, dest)

        if isinstance(source, Bucket):
            source = source.notify_subscription

        if not (isinstance(source, Flow) or isinstance(dest, Flow)):
            raise RuntimeError("edges must pass through a task")

        if isinstance(source, Subject):
            raise SeaplaneError(
                "the first argument to edge must be a Task, a Dag, or a Subscription"
            )

        if not (isinstance(dest, Flow) or isinstance(dest, Subject)):
            raise SeaplaneError("the second argument to edge must be a Task or a Subject")

        if isinstance(source, Flow) and isinstance(dest, Flow):
            if isinstance(source.subject, _FlowSubject):
                # TODO: Conditional dispatch will require addresses other than "*"
                source = source.subject.flow_subscription("*")
            else:
                raise SeaplaneError(
                    f"can't listen to task subject {source.subject.subject} automatically."
                    " To listen to this, you'll need to use an explicit Subscription"
                    " and write the Seaplane carrier filter yourself"
                )

        if isinstance(source, Flow) and isinstance(dest, Subject):
            source.subject = dest

        elif isinstance(source, Subscription) and isinstance(dest, Flow):
            dest.subscribe(source)
        else:
            # Don't trust the type system!
            raise RuntimeError(
                f"cannot wire {source} to {dest}."
                " The source of an edge must be a Subscription or a Flow"
            )


class Bucket:
    """
    A reference to a bucket and it's associated notification subscription.

    Get a bucket by asking the app to query the Seaplane infrastructure, like this:

    app = App("bucket-demo-app")
    dag = app.dag("dag")

    # This queries the Seaplane infrastructure, and may creaet a bucket
    # if one doesn't exist already
    bucket = app.bucket("bucket-demo-bucket")

    # once you have a bucket in hand, it can be used as the source
    # of events for a flow
    dag.task(observe_bucket, [bucket])
    """

    def __init__(self, name: str, notify: str):
        self.name = name
        self.notify_subscription = Subscription(notify)


class App:
    """
    An App is a unit of deployment to Seaplane. Use an App to create
    and deploy deploy Dags, which in turn you will use to create and
    organize individual tasks.

    An App is associated with a set of endpoints you can use to listen
    to HTTP requests and push data out of your Seaplane application, and
    optional references to Seaplane object store buckets.
    """

    class OutEndpoint(Subject):
        """
        The output seaplane endpoint. Does not accept subscriptions.

        Get this by calling App.output()
        """

        def __init__(self, endpoint: str):
            super(App.OutEndpoint, self).__init__(
                f"_SEAPLANE_ENDPOINT.out.{endpoint}."
                '${! meta("_seaplane_output_id") }'
                '${! meta("_seaplane_batch_hierarchy") }'
            )

    class InEndpoint(Subscription):
        """
        Endpoint represents the Subject of a seaplane input endpoint.

        Unlike most subscriptions, tasks subscribing to the seaplane input endpoint are
        configured to receive only new messages, rather than pull all messages
        from their upstream peers in order.

        Get one of these with App.input()
        """

        def __init__(self, endpoint: str):
            super(App.InEndpoint, self).__init__(
                f"_SEAPLANE_ENDPOINT.in.{endpoint}.>", deliver="new"
            )
            self.endpoint = endpoint

    # TODO: change the singleton to a REGISTRY approach, there is no real
    # TODO: need to enforce single-app processes.
    _instance: Optional["App"] = None

    def __init__(self, name: str, name_prefix: Optional[str] = None):
        if App._instance is not None:
            raise SeaplaneError(
                "you should only define a single app in your program."
                " {App._instance.name} is already defined"
            )

        if name_prefix is None:
            name_prefix = config.name_prefix

        self.name_prefix = name_prefix
        self.name = name_prefix + name
        self.dag_registry: Dict[str, Dag] = {}
        self.buckets: Set[Bucket] = set()
        self.input_endpoint = self.InEndpoint(self.name)
        self.output_endpoint = self.OutEndpoint(self.name)
        App._instance = self

    @classmethod
    def instance(cls) -> Optional["App"]:
        return cls._instance

    def bucket(self, bucket_name: str) -> Bucket:
        """
        Return a notify-capable bucket.

        Makes a network request to the Seaplane object store. Will
        attempt to create a new bucket if one doesn't exist, and may
        fail with an Exception if there is a service failure or if
        the named bucket exists but is not configured to send notifications.
        """

        notify = create_bucket_if_needed(self.name, bucket_name)
        b = Bucket(bucket_name, notify)
        self.buckets.add(b)
        return b

    def dag(self, dagname: str) -> Dag:
        prefixed_name = self.name_prefix + dagname
        if prefixed_name in self.dag_registry:
            raise SeaplaneError(
                f'there is already a dag named "{prefixed_name}" in application "{self.name}".'
                " The dags in an application must have unique names."
            )

        ret = Dag(prefixed_name)
        self.dag_registry[ret.name] = ret
        return ret

    def respond(self, tail: Union[Dag, Flow]) -> None:
        dag = tail.dag if isinstance(tail, Flow) else tail
        dag.edge(tail, self.output())

    def input(self) -> InEndpoint:
        """Return the "in" `Endpoint` for this Dag."""
        return self.input_endpoint

    def output(self) -> OutEndpoint:
        """Return the "out" `Endpoint` for this Dag."""
        return self.output_endpoint

    def run(self) -> None:
        """
        Run the application as the main work of a process.

        Reads command line arguments and the INSTANCE_NAME environment variable. If INSTANCE_NAME
        is present, and no arguments are provided, will attempt to execute the associated task.
        """
        # This has a bunch of circular dependencies but the ergonomics of `app.run()`
        # seem to make it worthwhile.
        import sys
        import toml

        import seaplane.deploy
        import seaplane.run_load_dotenv

        command = None
        if len(sys.argv) > 1:
            command = sys.argv[1]

        instance_name = os.getenv("INSTANCE_NAME")
        if command is None and instance_name:
            task = None
            for dag in self.dag_registry.values():
                if instance_name in dag.flow_registry:
                    task = dag.flow_registry[instance_name]
                    break

            if task is None:
                raise RuntimeError(f"no task instance named {instance_name} found")

            execute(task.instance_name, task.work)

        elif command == "deploy":
            pyproject = toml.loads(open("pyproject.toml", "r").read())
            project_directory_name = pyproject["tool"]["poetry"]["name"]
            seaplane.deploy.deploy(self, project_directory_name)
        elif command == "destroy":
            seaplane.deploy.destroy(self)
        elif command == "status":
            status()
        else:
            if command is not None:
                print(f'command "{command}" not supported in this version')

            print(
                f"Usage: {sys.argv[0]} COMMAND"
                """

Commands:
    deploy    deploys your application to Seaplane
    destroy   halts your application on Seaplane
"""
            )
