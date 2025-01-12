import gradio as gr
from orchestrator import orchestrate

def generate_report(topic):
    """
    Executes the workflow and generates a report.

    Args:
        topic (str): The topic for analysis.

    Returns:
        str: Path to the generated report.
    """
    try:
        return orchestrate(topic)
    except Exception as e:
        print(f"Error: {e}")
        return None

iface = gr.Interface(
    fn=generate_report,
    inputs=gr.Textbox(label="Enter Topic", placeholder="e.g., AI startups in healthcare from 2020-2025"),
    outputs=gr.File(label="Download Report"),
    title="AI Startup Analysis Tool",
    description="Analyze AI startups and generate a comprehensive PDF report."
)

if __name__ == "__main__":
    iface.launch()
