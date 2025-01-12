from smolagents import ToolCallingAgent, ManagedAgent, DuckDuckGoSearchTool

def get_research_agent(shared_model):
    """
    Create a research agent using the shared model.

    Args:
        shared_model (dict): Shared model and tokenizer.

    Returns:
        ManagedAgent: The research agent.
    """
    web_agent = ToolCallingAgent(
        tools=[DuckDuckGoSearchTool()],
        model=shared_model["model"],
        max_steps=10,
    )
    return ManagedAgent(
        agent=web_agent,
        name="research",
        description="Aggregates and summarizes web data using the shared model.",
    )
