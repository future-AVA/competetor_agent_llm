import pandas as pd
import matplotlib.pyplot as plt

def generate_visualization(data):
    """
    Generate a bar chart for SWOT sentiment distribution.

    Args:
        data (dict): Analysis data.

    Returns:
        str: Path to the visualization image.
    """
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

def get_visualization_agent(shared_model):
    """
    Create a visualization agent using the shared model.

    Args:
        shared_model (dict): Shared model and tokenizer.

    Returns:
        ManagedAgent: The visualization agent.
    """
    # No tools for this agent as it generates visualizations.
    return {"model": shared_model["model"], "description": "Visualization Agent"}
