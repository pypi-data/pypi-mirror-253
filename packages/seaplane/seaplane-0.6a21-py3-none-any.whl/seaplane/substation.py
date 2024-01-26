from seaplane.errors import SeaplaneError
from seaplane.kv import kv_store
from seaplane.object import ObjectStorageAPI
from seaplane.pipes import App, EdgeFrom, Subscription
from typing import Any, Dict, Generator, List, Optional

import json
import os
import requests

SUBSTATION_RESULTS_STREAM = "_SEAPLANE_AI_RESULTS"


class Substation:
    """
    Class for handling requests to and responses from Substation.

    See docstring for `make_request` for expected input and list of supported models.
    """

    def __init__(self, app_name: str, dag_name: Optional[str] = None):
        self.app_division = f"{app_name}"
        if dag_name is not None:
            self.app_division += f"-{dag_name}"
        self.request_store = f"_SP_REQUEST_{app_name}"
        self.response_store = f"_SP_RESPONSE_{app_name}"

    def results_stream(self) -> str:
        """
        Returns a string with the substation results stream
        """
        return SUBSTATION_RESULTS_STREAM

    def get_model(self, input_data: Dict[str, Any]) -> Dict[Any, Any]:
        """
        Returns headers and parameters for the selected model
        """
        model_name = input_data.get("model", "None").lower()
        headers = {"content-type": "application/json", "X-Division": self.app_division}
        data = {}

        # Default embeddings model (https://replicate.com/replicate/all-mpnet-base-v2)
        if model_name in (
            "replicate/all-mpnet-base-v2",
            "all-mpnet-base-v2",
            "embeddings",
        ):
            headers[
                "X-Version"
            ] = "b6b7585c9640cd7a9572c6e129c9549d79c9c31f0d3fdce7baac7c67ca38f305"
            for param in ("text", "text_batch"):
                value = input_data.get(param)
                if value:
                    data[param] = value

        # Zephyr-7B (https://replicate.com/tomasmcm/zephyr-7b-beta)
        elif model_name in (
            "tomasmcm/zephyr-7b-beta",
            "zephyr-7b-beta",
            "zephyr-7b",
        ):
            headers[
                "X-Version"
            ] = "961cd6665b811d0c43c0b9488b6dfa85ff5c7bfb875e93b4533e4c7f96c7c526"
            for param in (
                "prompt",
                "max_new_tokens",
                "temperature",
                "top_p",
                "top_k",
                "presence_penalty",
            ):
                value = input_data.get(param)
                if value:
                    data[param] = value

        # Mistral-7b-instruct (https://replicate.com/mistralai/mistral-7b-instruct-v0.1)
        elif model_name in (
            "mistralai/mistral-7b-instruct-v0.1",
            "mistral-7b-instruct-v0.1",
            "mistral-7b-instruct",
        ):
            headers[
                "X-Version"
            ] = "5fe0a3d7ac2852264a25279d1dfb798acbc4d49711d126646594e212cb821749"
            for param in (
                "prompt",
                "max_new_tokens",
                "min_new_tokens",
                "temperature",
                "top_p",
                "top_k",
                "repetition_penalty",
                "stop_sequences",
                "seed",
                "prompt_template",
            ):
                value = input_data.get(param)
                if value:
                    data[param] = value

        # BAAI/bge-large-en-v1.5 (https://replicate.com/nateraw/bge-large-en-v1.5)
        elif model_name in ("nateraw/bge-large-en-v1.5", "bge-large-en-v1.5"):
            headers[
                "X-Version"
            ] = "9cf9f015a9cb9c61d1a2610659cdac4a4ca222f2d3707a68517b18c198a9add1"
            for param in (
                "texts",
                "batch_size",
                "normalize_embeddings",
            ):  # leaving out path, convert_to_numpy as unsupported
                value = input_data.get(param)
                if value:
                    data[param] = value

        # CodeLlama-13b-Instruct (https://replicate.com/meta/codellama-13b-instruct)
        elif model_name in ("meta/codellama-13b-instruct", "codellama-13b-instruct"):
            headers[
                "X-Version"
            ] = "a5e2d67630195a09b96932f5fa541fe64069c97d40cd0b69cdd91919987d0e7f"
            for param in (
                "prompt",
                "system_prompt",
                "max_tokens",
                "temperature",
                "top_p",
                "top_k",
                "frequency_penalty",
                "presence_penalty",
                "repeat_penalty",
            ):
                value = input_data.get(param)
                if value:
                    data[param] = value

        # CodeLlama-34b-Python (https://replicate.com/meta/codellama-34b-python)
        elif model_name in ("meta/codellama-34b-python", "codellama-34b-python"):
            headers[
                "X-Version"
            ] = "e4cb69045bdb604862e80b5dd17ef39c9559ad3533e9fd3bd513cc68ff023656"
            for param in (
                "prompt",
                "max_tokens",
                "temperature",
                "top_p",
                "top_k",
                "frequency_penalty",
                "presence_penalty",
                "repeat_penalty",
            ):
                value = input_data.get(param)
                if value:
                    data[param] = value

        # Stable Diffusion 2.1 (https://replicate.com/stability-ai/stable-diffusion)
        elif model_name in (
            "stability-ai/stable-diffusion-2-1",
            "stability-ai/stable-diffusion",
            "stable-diffusion",
        ):
            headers[
                "X-Version"
            ] = "ac732df83cea7fff18b8472768c88ad041fa750ff7682a21affe81863cbe77e4"
            for param in (
                "prompt",
                "height",
                "width",
                "negative_prompt",
                "num_outputs",
                "num_inference_steps",
                "guidance_scale",
                "scheduler",
                "seed",
            ):
                value = input_data.get(param)
                if value:
                    data[param] = value

        # stability-ai/sdxl (https://replicate.com/stability-ai/sdxl)
        elif model_name in ("stability-ai/sdxl", "sdxl"):
            headers[
                "X-Version"
            ] = "39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b"
            for param in (
                "prompt",
                "negative_prompt",
                "image",
                "mask",
                "width",
                "height",
                "num_outputs",
                "scheduler",
                "num_inference_steps",
                "guidance_scale",
                "prompt_strength",
                "seed",
                "refine",
                "high_noise_frac",
                "refine_steps",
                "apply_watermark",
                "lora_scale",
                "disable_safety_checker",
            ):
                value = input_data.get(param)
                if value:
                    data[param] = value

        # andreasjansson/stable-diffusion-inpainting
        #  (https://replicate.com/andreasjansson/stable-diffusion-inpainting)
        elif model_name in (
            "andreasjansson/stable-diffusion-inpainting",
            "stable-diffusion-inpainting",
        ):
            headers[
                "X-Version"
            ] = "e490d072a34a94a11e9711ed5a6ba621c3fab884eda1665d9d3a282d65a21180"
            for param in (
                "prompt",
                "negative_prompt",
                "image",
                "mask",
                "invert_mask",
                "num_outputs",
                "num_inference_steps",
                "guidance_scale",
                "seed",
            ):
                value = input_data.get(param)
                if value:
                    data[param] = value

        # openai/whisper (https://replicate.com/openai/whisper)
        elif model_name in ("openai/whisper", "whisper"):
            headers[
                "X-Version"
            ] = "4d50797290df275329f202e48c76360b3f22b08d28c196cbc54600319435f8d2"
            for param in (
                "audio",
                "transcription",
                "translate",
                "language",
                "temperature",
                "patience",
                "suppress_tokens",
                "initial_prompt",
                "condition_on_previous_text",
                "temperature_increment_on_fallback",
                "compression_ratio_threshold",
                "logprob_threshold",
                "no_speech_threshold",
            ):
                value = input_data.get(param)
                if value:
                    data[param] = value

        # ResNet-50 (https://replicate.com/replicate/resnet)
        elif model_name in ("replicate/resnet", "resnet", "resnet-50"):
            headers[
                "X-Version"
            ] = "dd782a3d531b61af491d1026434392e8afb40bfb53b8af35f727e80661489767"
            for param in ("image",):
                value = input_data.get(param)
                if value:
                    data[param] = value

        # DEFAULT: meta/llama-2-70b-chat (https://replicate.com/meta/llama-2-70b-chat)
        # elif model_name in ("meta/llama-2-70b-chat", "llama-2-70b-chat", "Llama-2 (70B)"):
        else:
            headers[
                "X-Version"
            ] = "02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3"
            for param in (
                "prompt",
                "system_prompt",
                "max_new_tokens",
                "min_new_tokens",
                "temperature",
                "top_p",
                "top_k",
                "stop_sequences",
                "seed",
            ):
                value = input_data.get(param)
                if value:
                    data[param] = value

        return {"headers": headers, "data": data}

    def make_request(self, input_data: Dict[str, Any]) -> Dict[Any, Any]:
        """
        Makes the request to substation and returns the request information, including ID.

        `input_data` (Dict/JSON) must include `"model"` (see below) and at least one input:

          For LLMs, usually `"prompt"` and optional args, like `"temperature"`.

          For embeddings, `"text"` (string) or `"texts"`/`"text_batch"` (JSON list of strings).

        Supported models:
          `"all-mpnet-base-v2"` (also: `"embeddings"`) /
          `"zephyr-7b"` /
          `"mistral-7b-instruct"` /
          `"bge-large-en-v1.5"` /
          `"codellama-13b-instruct"` /
          `"codellama-34b-python"` /
          `"stable-diffusion-2-1"` /
          `"sdxl"` /
          `"stable-diffusion-inpainting"` /
          `"whisper"` /
          `"resnet-50"` /
          `"llama-2-70b-chat"` (default model)
        """
        model_params = self.get_model(input_data)

        proxy_addr = os.getenv("SEAPLANE_PROXY_ADDRESS", "localhost:4195")
        url = f"http://{proxy_addr}/predictions"

        resp = requests.post(url, headers=model_params["headers"], json=model_params["data"])
        if resp.status_code != 200:
            raise SeaplaneError("Error making substation request")

        request_data = {"request": resp.json(), "input_data": input_data}
        return request_data

    def get_response(self, msg: Any) -> Generator[Any, None, None]:
        """
        Use this task to get the completed substation response
        """
        data = json.loads(msg.body)

        # If this is request data from the previous task it will have "request"
        #  See if there is matching response data in KV
        request = data.get("request")
        if request:
            if kv_store.exists(self.response_store, request["id"]):
                response = json.loads(kv_store.get_key(self.response_store, request["id"]))
                data.update({"response": response})
                kv_store.delete_key(self.response_store, request["id"])

                # clean up output a little
                if type(data["output"]) is list:
                    if type(data["output"][0]) is str:
                        output = "".join(data["output"])
                        data["output"] = output
                        if "https://replicate.delivery" in output:
                            obj = ObjectStorageAPI()
                            response = requests.get(output)
                            obj_name = (
                                f"{msg.meta['_seaplane_request_id']}.{output.split('.')[-1]}"
                            )
                            bucket = f"{self.app_division.lower()}-downloads"
                            if bucket not in obj.list_buckets():
                                print(f"creating bucket {bucket}")
                                obj.create_bucket(bucket)
                            obj.upload(bucket, obj_name, response.content)
                            data["output"] = {"bucket": bucket, "object": obj_name}
                for key in (
                    "request",
                    "logs",
                    "urls",
                    "version",
                    "webhook",
                    "webhook_events_filter",
                ):
                    data.pop(key, "")

                yield json.dumps(data).encode()
            else:
                # store request_id and batch_hierarchy for later output
                request.update(
                    {
                        "input_data": data["input_data"],
                        "seaplane_request_id": msg.meta["_seaplane_request_id"],
                        "seaplane_batch_hierarchy": msg.meta["_seaplane_batch_hierarchy"],
                    }
                )
                kv_store.set_key(self.request_store, request["id"], json.dumps(request).encode())
                yield

        # If this is a response from Substation it will have "output"
        #  See if there matching request data in KV
        if "output" in data:
            if kv_store.exists(self.request_store, data["id"]):
                request = json.loads(kv_store.get_key(self.request_store, data["id"]))
                # data.update({"request": request})  # cleaner output, could go back in later
                kv_store.delete_key(self.request_store, data["id"])

                # restore the original request_id and batch_hierarchy
                seaplane_request_id = request.pop("seaplane_request_id")
                seaplane_batch_hierarchy = request.pop("seaplane_batch_hierarchy")

                # restore user input data
                data.update({"input_data": request["input_data"]})

                # clean up output a little
                if type(data["output"]) is list:
                    if type(data["output"][0]) is str:
                        output = "".join(data["output"])
                        data["output"] = output
                        if "https://replicate.delivery" in output:
                            obj = ObjectStorageAPI()
                            response = requests.get(output)
                            obj_name = f"{seaplane_request_id}.{output.split('.')[-1]}"
                            bucket = f"{self.app_division.lower()}-downloads"
                            if bucket not in obj.list_buckets():
                                print(f"creating bucket {bucket}")
                                obj.create_bucket(bucket)
                            obj.upload(bucket, obj_name, response.content)
                            data["output"] = {"bucket": bucket, "object": obj_name}
                for key in (
                    "logs",
                    "urls",
                    "version",
                    "webhook",
                    "webhook_events_filter",
                ):
                    data.pop(key, "")

                ret = msg.result(json.dumps(data).encode())
                ret.output_id = seaplane_request_id
                ret.override_batch_hierarchy(seaplane_batch_hierarchy)
                yield ret
            else:
                kv_store.set_key(self.response_store, data["id"], json.dumps(data).encode())
                yield


def substation_dag(app: App, name: str, input_list: Optional[List[EdgeFrom]] = None) -> Any:
    dag = app.dag(name)
    if input_list is None:
        input_list = [app.input()]
    app_dag_name = f"{app.name}-{name}"
    substation = Substation(app.name, name)

    def make_request(msg: Any) -> Any:
        input_data = json.loads(msg.body)
        request_data = substation.make_request(input_data)
        yield json.dumps(request_data).encode()

    request = dag.task(make_request, input_list)

    response_sub = f"{substation.results_stream()}.{app_dag_name}.>"
    response = dag.task(
        substation.get_response, [request, Subscription(response_sub, deliver="new")]
    )

    dag.respond(response)

    return dag
