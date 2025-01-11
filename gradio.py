import gradio as gr
from orchestrator import orchestrate

def generate_report(topic):
    """
    Gradio interface function to execute the workflow and generate a report.
    
    Args:
        topic (str): The topic to research and analyze.

    Returns:
        str: The path to the generated PDF report.
    """
    try:
        print(f"Generating report for topic: {topic}")
        report_path = orchestrate(topic)
        print(f"Report successfully generated: {report_path}")
        return report_path
    except Exception as e:
        print(f"Error occurred during report generation: {str(e)}")
        return "An error occurred while generating the report. Please try again."

# Define the Gradio interface
iface = gr.Interface(
    fn=generate_report,
    inputs=gr.Textbox(
        label="Enter Topic",
        placeholder="e.g., AI startups in healthcare from 2020-2025",
    ),
    outputs=gr.File(label="Download Report"),
    title="AI Startup Analysis Tool",
    description="Analyze AI startups and generate a comprehensive PDF report with SWOT analysis and visualizations.",
    theme="compact",
)

if __name__ == "__main__":
    # Launch the Gradio interface
    iface.launch()
