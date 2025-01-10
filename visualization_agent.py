import pandas as pd
import matplotlib.pyplot as plt

def visualization_agent_function(analysis_result):
    """Generates visualizations from analysis results."""
    swot = analysis_result["swot"]
    df = pd.DataFrame(swot)
    
    # Create a bar chart for strengths and weaknesses
    df["sentiment"] = df["swot"].apply(lambda x: "Strength" if "strength" in x.lower() else "Weakness")
    sentiment_count = df["sentiment"].value_counts()
    
    plt.figure(figsize=(8, 5))
    sentiment_count.plot(kind="bar")
    plt.title("SWOT Sentiment Distribution")
    plt.ylabel("Count")
    plt.savefig("swot_sentiment.png")
    
    return {"visualization": "swot_sentiment.png"}
