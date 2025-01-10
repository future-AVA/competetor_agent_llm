from smolagents import ToolCallingAgent
from hf_api_model import HfApiModel

def analysis_agent_function(research_data):
    """Performs SWOT analysis and compares startups."""
    model = HfApiModel(model_id="distilbert-base-uncased-finetuned-sst-2-english")  # Sentiment analysis model
    startups = research_data["data"]
    
    # SWOT analysis for each startup
    swot_analysis = []
    for startup in startups.splitlines():
        swot = model.run(f"Perform a SWOT analysis for: {startup}")
        swot_analysis.append({"startup": startup, "swot": swot})
    
    # Overall sentiment analysis
    sentiment = model.run(f"Analyze sentiment for the following data: {startups}")
    return {"swot": swot_analysis, "sentiment": sentiment}
