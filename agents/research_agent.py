from smolagents import ToolCallingAgent, ManagedAgent, DuckDuckGoSearchTool
from smoltools.jinaai import scrape_page_with_jina_ai
from hf_api_model import get_model

def get_research_agent():
    """Create a research agent using a summarization model."""
    model = get_model(model_id="facebook/bart-large-cnn")  # Summarization model
    web_agent = ToolCallingAgent(
        tools=[DuckDuckGoSearchTool(), scrape_page_with_jina_ai],
        model=model,
        max_steps=10,
    )
    return ManagedAgent(
        agent=web_agent,
        name="research",
        description="Fetches and summarizes startup data from the web.",
    )
