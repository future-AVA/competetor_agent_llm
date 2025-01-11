from smolagents import HfApiModel
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_model(model_id):
    """Create and return a configured Hugging Face model."""
    return HfApiModel(model_id=model_id, api_key=os.getenv("HF_TOKEN"))
