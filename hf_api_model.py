from transformers import AutoModelForCausalLM, AutoTokenizer
import os
import logging

# Enable logging for detailed feedback
logging.basicConfig(level=logging.INFO)

def load_shared_model(model_id="tiiuae/falcon-7b-instruct"):
    """
    Load a Hugging Face model for CPU inference with optimizations.

    Args:
        model_id (str): The Hugging Face model ID.

    Returns:
        dict: A dictionary containing the model and tokenizer.
    """
    logging.info(f"Loading shared model: {model_id}...")

    hf_token = os.getenv("HF_TOKEN")  # Load token from environment, if required
    try:
        # Load tokenizer
        tokenizer = AutoTokenizer.from_pretrained(model_id, use_auth_token=hf_token)

        # Load model
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            device_map="cpu",             # Use CPU for inference
            use_auth_token=hf_token,      # For private models
            low_cpu_mem_usage=True        # Optimize memory usage
        )

        logging.info("Model and tokenizer loaded successfully.")
        return {"model": model, "tokenizer": tokenizer}

    except Exception as e:
        logging.error(f"Error loading model: {e}")
        raise
