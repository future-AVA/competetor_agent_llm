from smolagents import ToolCallingAgent, ManagedAgent
import pandas as pd
import matplotlib.pyplot as plt

def generate_visualization(data):
    """Create a bar chart for SWOT sentiment distribution."""
    df = pd.DataFrame(data)
    df["type"] = df["swot"].apply(lambda x: "Strength" if "strength" in x.lower() else "Weakness")
    counts = df["type"].value_counts()

    plt.figure(figsize=(8, 5))
    counts.plot(kind="bar")
    plt.title("SWOT Analysis Distribution")
    plt.ylabel("Count")
    output_path = "generated_reports/swot_analysis.png"
    plt.savefig(output_path)
    return output_path

def get_visualization_agent():
    """Create a visualization agent."""
    model = get_model(model_id="gpt-neo-125M")  # A lightweight model for simple tasks
    visualization_agent = ToolCallingAgent(
        tools=[],
        model=model,
        max_steps=10,
    )
    return ManagedAgent(
        agent=visualization_agent,
        name="visualization",
        description="Generates visualizations for analysis results.",
    )
