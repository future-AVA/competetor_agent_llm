from hf_api_model import load_shared_model
from agents.research_agent import get_research_agent
from agents.analysis_agent import get_analysis_agent
from agents.visualization_agent import generate_visualization, get_visualization_agent
from agents.report_agent import generate_pdf_report

def orchestrate(topic):
    """
    Orchestrate the workflow for the given topic.

    Args:
        topic (str): The topic for analysis.

    Returns:
        str: Path to the generated PDF report.
    """
    # Load shared model
    shared_model = load_shared_model(model_id="tiiuae/falcon-7b-instruct")

    # Initialize agents
    research_agent = get_research_agent(shared_model)
    analysis_agent = get_analysis_agent(shared_model)
    visualization_agent = get_visualization_agent(shared_model)

    # Execute workflow
    research_data = research_agent.agent.run(f"Aggregate data on {topic}")
    analysis_data = analysis_agent.agent.run(f"Perform SWOT analysis on: {research_data}")
    visualization_path = generate_visualization(analysis_data)
    report_path = generate_pdf_report(research_data, analysis_data, visualization_path)

    return report_path
