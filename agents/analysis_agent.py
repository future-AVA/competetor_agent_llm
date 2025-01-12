from smolagents import ToolCallingAgent, ManagedAgent

def get_analysis_agent(shared_model):
    """
    Create an analysis agent using the shared model.

    Args:
        shared_model (dict): Shared model and tokenizer.

    Returns:
        ManagedAgent: The analysis agent.
    """
    analysis_agent = ToolCallingAgent(
        tools=[],
        model=shared_model["model"],
        max_steps=10,
    )
    return ManagedAgent(
        agent=analysis_agent,
        name="analysis",
        description="Performs SWOT and sentiment analysis using the shared model.",
    )
