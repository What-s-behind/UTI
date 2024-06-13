import requests

OLLAMA_URL_LOCAL = "http://localhost:11434"
try: 
    ollama_local_signal = str.encode('Ollama is running')
    response = requests.get(OLLAMA_URL_LOCAL).content
    if response != ollama_local_signal: 
        raise ImportError("Ollama is not installed.")
except ImportError:
    raise ValueError(
        "Gemini is not installed. Please install it with "
        "`pi")
class OllamaAgent: 
    ...