from fpdf import FPDF
from hf_api_model import HfApiModel

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'AI Startup Analysis Report', align='C', ln=1)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def add_section(self, title, content):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, ln=1)
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 10, content)
        self.ln()

def report_generation_agent_function(research_data, analysis_result, visualization_output):
    """Generate a detailed PDF report."""
    model = HfApiModel(model_id="meta-llama/Llama-2-7b-chat-hf")
    
    # Compile the report content
    prompt = f"""
    Generate a detailed report for AI startups in {research_data['topic']}:
    - Research Data: {research_data['data']}
    - SWOT Analysis: {analysis_result['swot']}
    - Sentiment Insights: {analysis_result['sentiment']}
    Include visualization: {visualization_output['visualization']}.
    """
    textual_report = model.run(prompt)

    # Generate PDF
    pdf = PDFReport()
    pdf.add_page()
    
    # Add sections
    pdf.add_section("Topic", research_data['topic'])
    pdf.add_section("Research Data", research_data['data'])
    pdf.add_section("SWOT Analysis", str(analysis_result['swot']))
    pdf.add_section("Sentiment Insights", str(analysis_result['sentiment']))

    # Add visualization
    pdf.image(visualization_output['visualization'], x=10, y=None, w=180)
    
    # Save the report
    output_file = "AI_Startup_Report.pdf"
    pdf.output(output_file)
    print(f"Report saved as {output_file}")

    return {"report": textual_report, "pdf_file": output_file}
