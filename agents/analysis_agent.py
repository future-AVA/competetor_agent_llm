from smolagents import ToolCallingAgent, ManagedAgent
from hf_api_model import get_model

def get_analysis_agent():
    """Create an analysis agent using a sentiment analysis model."""
    model = get_model(model_id="distilbert-base-uncased-finetuned-sst-2-english")  # Sentiment model
    analysis_agent = ToolCallingAgent(
        tools=[],
        model=model,
        max_steps=10,
    )
    return ManagedAgent(
        agent=analysis_agent,
        name="analysis",
        description="Performs SWOT and sentiment analysis on startup data.",
    )
