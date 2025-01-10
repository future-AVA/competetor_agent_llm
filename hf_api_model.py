import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class HfApiModel:
    def __init__(self, model_id):
        self.model_id = model_id
        self.api_key = os.getenv("HF_TOKEN")
        print(f"Initialized HfApiModel with ID: {model_id}")

    def run(self, prompt):
        # Simulate a call to the Hugging Face model
        print(f"Model {self.model_id} executing prompt: {prompt}")
        return f"Response from {self.model_id}: Generated output for '{prompt}'"
