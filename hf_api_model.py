import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class HfApiModel:
    def __init__(self, model_id):
        self.model_id = model_id
        self.api_key = os.getenv("HF_TOKEN")
        print(f"Initialized HfApiModel with ID: {model_id}")

    def run(self, prompt):
        # Simulated model execution (replace with Hugging Face API call if needed)
        print(f"Running model {self.model_id} with prompt: {prompt}")
        return f"Generated response for: {prompt}"
