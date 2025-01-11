from smolagents import CodeAgent
from agents.research_agent import get_research_agent
from agents.analysis_agent import get_analysis_agent
from agents.visualization_agent import generate_visualization, get_visualization_agent
from agents.report_agent import generate_pdf_report, get_report_agent

def get_orchestrator():
    """
    Returns a configured CodeAgent for orchestrating the workflow.
    This CodeAgent manages all the individual agents.
    """
    # Create CodeAgent with all managed agents
    orchestrator = CodeAgent(
        tools=[],  # Add any additional tools here if necessary
        model=None,  # CodeAgent itself doesn't require a model
        managed_agents=[
            get_research_agent(),
            get_analysis_agent(),
            get_visualization_agent(),
            get_report_agent(),
        ],
        additional_authorized_imports=["time", "pandas", "matplotlib"],  # Add necessary imports
    )
    return orchestrator

def orchestrate(topic):
    """
    Executes the workflow for the given topic using CodeAgent to manage all agents.
    
    Workflow:
    - Research: Aggregate data on the topic.
    - Analysis: Perform SWOT and sentiment analysis.
    - Visualization: Generate data visualizations.
    - Report Generation: Create a PDF report summarizing all findings.

    Args:
        topic (str): The topic to research and analyze.

    Returns:
        str: The path to the generated PDF report.
    """
    # Get the orchestrator
    orchestrator = get_orchestrator()

    print("[1/4] Running research agent...")
    research_data = orchestrator.run(f"Aggregate data on {topic}")

    print("[2/4] Running analysis agent...")
    analysis_data = orchestrator.run(f"Perform SWOT analysis on: {research_data}")

    print("[3/4] Running visualization agent...")
    visualization_path = generate_visualization(analysis_data["swot"])

    print("[4/4] Running report generation agent...")
    report_path = generate_pdf_report(research_data, analysis_data, visualization_path)

    print(f"Workflow completed. Report saved at: {report_path}")
    return report_path

if __name__ == "__main__":
    # Example usage
    topic = "AI startups in healthcare from 2020-2025"
    print(f"Orchestrating workflow for topic: {topic}")
    report_path = orchestrate(topic)
    print(f"Final report available at: {report_path}")
