from smolagents import (
    CodeAgent,
    ToolCallingAgent,
    LiteLLMModel,
    ManagedAgent,
    SearchEngineTool
)
from smoltools.jinaai import scrape_page_with_jina_ai, search_facts_with_jina_ai
from textblob import TextBlob
from sklearn.ensemble import RandomForestClassifier 
from dotenv import load_dotenv
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

load_dotenv()

# Initialize the model
model = LiteLLMModel(model_id="gpt-4o-mini")

# Research Agent: Enhanced with Google and LinkedIn specific search tools
research_agent = ToolCallingAgent(
    tools=[scrape_page_with_jina_ai, search_facts_with_jina_ai, SearchEngineTool(sources=["google", "linkedin"])],
    model=model,
    max_steps=10,
)

managed_research_agent = ManagedAgent(
    agent=research_agent,
    name="data_aggregator",
    description="Aggregates data from multiple sources, including real-time feeds and academic databases.",
)

# Analysis Agent: To perform SWOT analysis, extract insights, and apply predictive analytics
analysis_agent = ToolCallingAgent(
    tools=[],
    model=model,
)

def analyze_sentiment(text):
    """ Analyzes sentiment of the provided text. """
    blob = TextBlob(text)
    return {'polarity': blob.sentiment.polarity, 'subjectivity': blob.sentiment.subjectivity}

managed_analysis_agent = ManagedAgent(
    agent=analysis_agent,
    name="analysis_expert",
    description="Analyzes aggregated data to perform SWOT analysis, sentiment analysis, and make predictions.",
)

# Customization and Visualization Agent
customization_agent = ToolCallingAgent(
    tools=[],
    model=model
)

def generate_visualization(data):
    """ Generates data visualizations. """
    plt.figure(figsize=(10, 5))
    sns.barplot(x='Feature', y='Importance', data=data)
    plt.title('Feature Importance from Predictive Model')
    plt.savefig('feature_importance.png')
    plt.close()

managed_customization_agent = ManagedAgent(
    agent=customization_agent,
    name="customization_expert",
    description="Generates reports with customizable templates and sophisticated data visualizations.",
)

# Report Generator Agent: To create comprehensive reports
report_generator_agent = ToolCallingAgent(
    tools=[],
    model=model,
)

managed_report_generator = ManagedAgent(
    agent=report_generator_agent,
    name="report_writer",
    description="Generates detailed reports with insights, key feature comparisons, strategic recommendations, and follows up for deeper analysis.",
)

# Data Pipeline Manager
data_pipeline_manager = CodeAgent(
    tools=[],
    model=model,
    managed_agents=[managed_research_agent, managed_analysis_agent, managed_customization_agent, managed_report_generator],
    additional_authorized_imports=["re", "pandas", "matplotlib.pyplot", "seaborn", "sklearn.ensemble"],
)

def generate_ai_startup_report(topic, output_file="AI_Startup_Report.md"):
    """
    Generates a detailed report on AI startups by following these steps:
    1. Aggregate data from sources like Google and LinkedIn.
    2. Perform SWOT analysis, sentiment analysis, and predict future trends.
    3. Customize report templates and generate sophisticated data visualizations.
    4. Generate a comprehensive report with strategic recommendations.
    5. Follow up with automated prompts for further research if needed.
    
    Args:
        topic (str): The topic or title for the report
        output_file (str): The filename to save the report
    """
    result = data_pipeline_manager.run(f"""Create a detailed report on: {topic}
    1. Aggregate data from multiple sources, focusing on AI startups.
    2. Perform advanced analysis including sentiment and predictive analytics.
    3. Customize the report and visualize key data points.
    4. Generate a comprehensive report with strategic recommendations.
    5. Suggest follow-up topics based on findings.
    """)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)
    print(f"Report has been saved to {output_file}")
    
    return result

# Example usage
topic = "In-depth Market Analysis of AI Startups in Healthcare"
print(topic)
generate_ai_startup_report(topic)
