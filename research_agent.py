from smolagents import ToolCallingAgent, DuckDuckGoSearchTool
from smoltools.jinaai import scrape_page_with_jina_ai

def research_agent_function(topic):
    """Aggregates data from various sources."""
    model = HfApiModel(model_id="facebook/bart-large-cnn")  # Summarization model
    agent = ToolCallingAgent(
        tools=[DuckDuckGoSearchTool(), scrape_page_with_jina_ai],
        model=model
    )
    
    # Collect data using tools
    raw_data = agent.run(f"Search for AI startups in {topic}. Include name, location, website, and funding details.")
    
    # Summarize the collected data
    summarized_data = model.run(f"Summarize the following data: {raw_data}")
    return {"topic": topic, "data": summarized_data}
