import asyncio
from typing import Optional, List
from enum import Enum
import requests
import json
import websockets


class JobFailed(Exception):
    def __init__(self, message="Skymap Job Processing Job Failed"):
        super().__init__(message)

def snake_to_camel(s):
    parts = s.split('_')
    return parts[0] + ''.join(x.title() for x in parts[1:])

def convert_keys_to_camel_case(dictionary):
    if isinstance(dictionary, dict):
        new_dict = {}
        for key, value in dictionary.items():
            new_key = snake_to_camel(key)
            new_value = convert_keys_to_camel_case(value) if isinstance(value, (dict, list)) else value
            new_dict[new_key] = new_value
        return new_dict
    elif isinstance(dictionary, list):
        return [convert_keys_to_camel_case(item) for item in dictionary]
    else:
        return dictionary

class KeyValuePair():
    def __init__(self, name:str, value:str) -> None:
        self.name = name
        self.value = value

class ResourceType(Enum):
    GPU = "GPU"
    MEMORY = "MEMORY"
    VCPU = "VCPU"

class FileType(Enum):
    FILE = "FILE"
    FOLDER = "FOLDER"

class ResultType(Enum):
    RASTER = "RASTER"
    VECTOR = "VECTOR"

class ResourceRequirement():
    def __init__(self, value: str, type: ResourceType) -> None:
        self.type = type
        self.value = value

class JobConfig():
    def __init__(
            self, 
            definition:Optional[str]=None, 
            queue_name:Optional[str]=None, 
            command:Optional[List[str]]=None, 
            environment:Optional[List[KeyValuePair]]=None, 
            resource_requirements:Optional[List[ResourceRequirement]]=None
        ):
        self.definition = definition
        self.queue_name = queue_name
        self.resource_requirements = resource_requirements
        self.command = command
        self.environment = environment

class ProcessingInput():
    def __init__(self,name: str, source: str,destination: str, type: FileType, processor:Optional[JobConfig] = None):
        self.name = name
        self.source = source
        self.destination = destination
        self.type = type
        self.processor = processor

class Result():
    def __init__(self, type:ResourceType, destination:Optional[str]=None) -> None:
        self.type = type
        self.destination = destination

class ProcessingInput():
    def __init__(self,name: str, source: str,destination: str, type: str, processor:Optional[JobConfig] = None):
        self.name = name
        self.source = source
        self.destination = destination
        self.type = type
        self.processor = processor

class ProcessingOutput(ProcessingInput):
    def __init__(self, name: str, source: str, destination: str, type: FileType, processor: JobConfig | None = None, result:Optional[Result]=None):
        super().__init__(name, source, destination, type, processor)
        self.result = result

class Credential():
    def __init__(self, endpoint:str,ws_endpoint:str,secret_key:str, region:str):
        self.secret_key = secret_key
        self.region = region
        self.endpoint = endpoint
        self.ws_endpoint = ws_endpoint

class Processor(object):
    def __init__(self, 
        credential: Credential, 
        name: str, 
        main_job: JobConfig,
        input_processing_job: JobConfig = None,
        output_processing_job: JobConfig = None,
        is_persistent_storage: bool = False,
        storage_id: Optional[str] = None,
        processing_inputs: List[ProcessingInput] = [], 
        processing_outputs:List[ProcessingOutput] = [],
        execution_id = None
    ):
        self.credential = credential
        self.name = name
        self.main_job = main_job
        self.is_persistent_storage = is_persistent_storage
        self.storage_id = storage_id
        self.processing_inputs = processing_inputs 
        self.processing_outputs = processing_outputs
        self.region = self.credential.region
        self.execution_id = execution_id
        self.input_processing_job = input_processing_job
        self.output_processing_job = output_processing_job

    def to_dict(self):
        def remove_none(obj):
            if isinstance(obj, list):
                for i in range(len(obj) - 1, -1, -1):
                    if obj[i] is None:
                        del obj[i]
                    else:
                        remove_none(obj[i])
            elif isinstance(obj, set):
                obj.discard(None)
                for elem in obj:
                    remove_none(elem)
            elif isinstance(obj, dict):
                for k, v in list(obj.items()):
                    if k is None or v is None:
                        del obj[k]
                    else:
                        remove_none(v)
        payload = json.loads(json.dumps(self, default=lambda o: o.__dict__))
        remove_none(payload)
        del payload["credential"]
        if "execution_id" in payload:
            del payload["execution_id"]
        return convert_keys_to_camel_case(payload)

    async def wait(self):
        headers = [
            ("x-secret-key", self.credential.secret_key),
            ("execution-id", self.execution_id),
        ]
        try:
            async with websockets.connect(self.credential.ws_endpoint, extra_headers=headers) as websocket:
                print("Connected to Skymap Job Procesing Network")
                while True:
                    message:str = await websocket.recv()
                    print(message)
                    if "EXECUTION_FAILED" in message or "EXECUTION_SUCCEEDED" in message:
                        await websocket.close()
                        if "EXECUTION_FAILED" in message:
                            raise JobFailed(':'.join(message.split(":")[1:]))
        except websockets.ConnectionClosed as e:
            print(f"Connection closed")
        except JobFailed as e:
            raise e

    def run(self, wait:bool= True):
        print(self.to_dict())
        if(self.execution_id is None):
            try:
                headers = {"x-secret-key": self.credential.secret_key}
                res = requests.post(f"{self.credential.endpoint}/api/executions", json=self.to_dict(), headers=headers)
                if not res.ok:
                    raise Exception(res.text)
                print("Job created successfully!")
                data = res.json()["data"]
                self.execution_id = data["id"]
                print(f"Execution ID: {self.execution_id}")
                res = requests.post(f"{self.credential.endpoint}/api/executions/{self.execution_id}/start", headers=headers)
                if not res.ok:
                    raise Exception(res.text)
                print("Start processing job.............")
            except requests.exceptions.ConnectionError as e:
                raise Exception("Can not connect to job server")
            except Exception as e:
                raise e
        if(wait):
            loop = asyncio.new_event_loop()
            task = loop.create_task(self.wait())
            loop.run_until_complete(task)



