import os, io
import json
import binascii
import requests

from os import PathLike
from pathlib import Path
from base64 import b64encode, b64decode

from typing import Any, Union, Optional

OLLAMA_URL_LOCAL = "http://localhost:11434"
OLLAMA_API = ["http://localhost:11434/api/generate", 
              "http://localhost:11434/api/chat"]

try: 
    response = requests.get(OLLAMA_URL_LOCAL).content
    ollama_local_signal = str.encode('Ollama is running')
    if response != ollama_local_signal: 
        raise ImportError("Ollama is not installed or something other than Ollama is running on this port.")
except:
    raise ValueError(
        "Ollama is not installed.")


class OllamaAgent: 
    
    def __init__(self): 
        self.model = "llava"
        self.headers = {
            "Content-Type": "application/json"
            }
    @classmethod
    def chat(self, prompt:str, 
             image_path:str): 
        payload = {
        "model":  self.model,
        "prompt": prompt, 
        "stream": False, 
        "images": [self._encode_image(image_path)]
        }
        try: 
            response = requests.post(url=OLLAMA_API[0], 
                                    headers=self.headers, 
                                    data=json.dumps(payload))
            response = json.loads(response.text)
            return response
        except Exception as err: 
            return err

    def _encode_image(self, image) -> str:

        if p := self._as_path(image):
            return b64encode(p.read_bytes()).decode('utf-8')

        try:
            b64decode(image, validate=True)
            return image if isinstance(image, str) else image.decode('utf-8')
        except (binascii.Error, TypeError):
            ...

        if b := self._as_bytesio(image):
            return b64encode(b.read()).decode('utf-8')

        raise ValueError('image must be bytes, path-like object, or file-like object')

    def _as_path(self, s: Optional[Union[str, PathLike]]) -> Union[Path, None]:
        if isinstance(s, str) or isinstance(s, Path):
            try:
                if (p := Path(s)).exists():
                    return p
            except Exception:
                ...
        return None


    def _as_bytesio(self, s: Any) -> Union[io.BytesIO, None]:
        if isinstance(s, io.BytesIO):
            return s
        elif isinstance(s, bytes):
            return io.BytesIO(s)
        return None

    