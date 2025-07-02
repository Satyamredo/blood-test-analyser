# llama_llm.py
import requests

class OllamaLLaMA3LLM:
    def __init__(self, model_name='local/llama3.2:1b', base_url='http://localhost:1143'):
        self.model_name = model_name
        self.base_url = base_url

    def run(self, prompt: str) -> str:
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False
        }

        print(f"Sending request to {self.base_url}/api/generate with payload: {payload}")
        response = requests.post(
            f"{self.base_url}/api/generate",
            json=payload
        )
        print(f"Received response: {response.status_code} - {response.text}")
        if response.status_code == 200:
            return response.json()["response"]
        else:
            raise Exception(f"Ollama Error: {response.text}")
