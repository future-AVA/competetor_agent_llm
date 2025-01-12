import gradio as gr
from agents.research_agent import aggregate_data
from agents.analysis_agent import perform_comparison_and_swot
from agents.visualization_agent import generate_visualizations
from agents.report_agent import generate_report

def generate_reports_pipeline(input_query):
    """
    Pipeline to generate detailed reports with plain text, visualizations, and tables.

    Args:
        input_query (str): Query for research (e.g., "AI startups in healthcare").

    Returns:
        str: Path to the generated PDF report.
    """
    # Step 1: Aggregate data
    company_data = aggregate_data(input_query)

    # Step 2: Perform SWOT analysis and comparison
    swot_results = perform_comparison_and_swot(company_data)

    # Step 3: Generate visualizations
    visualizations = generate_visualizations(company_data)

    # Step 4: Generate the final report
    report_path = generate_report(company_data, swot_results, visualizations)
    return report_path

# Gradio interface
with gr.Blocks() as interface:
    gr.Markdown("# AI Startup Analysis Tool")
    query_input = gr.Textbox(label="Enter Query", placeholder="e.g., AI startups in healthcare")
    generate_button = gr.Button("Generate Report")
    output_file = gr.File(label="Download Report")

    generate_button.click(
        fn=generate_reports_pipeline,
        inputs=query_input,
        outputs=output_file
    )

if __name__ == "__main__":
    interface.launch(share=True)
