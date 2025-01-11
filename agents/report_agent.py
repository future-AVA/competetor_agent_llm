from smolagents import ToolCallingAgent, ManagedAgent
from hf_api_model import get_model
from fpdf import FPDF

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

# Structured prompts inspired by your example
def get_report_prompt(research_data, analysis_data, visualization_path):
    """Return a structured prompt for report generation."""
    return f"""
    You are an expert in business and startup analysis. Using the following data, create a detailed, professional report:

    RESEARCH DATA
    {research_data}

    SWOT ANALYSIS
    {analysis_data['swot']}

    SENTIMENT INSIGHTS
    {analysis_data['sentiment']}

    VISUALIZATION
    Include the following visualization in the report: {visualization_path}.

    FORMAT
    1. Executive Summary
    2. Detailed Findings
       - Research Insights
       - SWOT Analysis
       - Sentiment Analysis
    3. Key Takeaways
    4. References (if applicable)
    """

def generate_pdf_report(research_data, analysis_data, visualization_path):
    """Generate a PDF report."""
    # Use LLaMA instruct model for report generation
    model = get_model(model_id="meta-llama/Llama-2-7b-chat-hf")  
    prompt = get_report_prompt(research_data, analysis_data, visualization_path)
    report_content = model.run(prompt)

    # Create the PDF
    pdf = PDFReport()
    pdf.add_page()
    pdf.add_section("Executive Summary", "Generate  Comparison analysis report.")
    pdf.add_section("Detailed Findings", report_content)
    pdf.image(visualization_path, x=10, y=None, w=180)

    # Save the PDF
    output_path = "generated_reports/AI_Startup_Report.pdf"
    pdf.output(output_path)
    return output_path

def get_report_agent():
    """Returns a ManagedAgent for generating PDF reports."""
    model = get_model(model_id="meta-llama/Llama-2-7b-chat-hf")
    report_agent = ToolCallingAgent(
        tools=[],
        model=model,
        max_steps=10,
    )
    return ManagedAgent(
        agent=report_agent,
        name="report",
        description="Generates a detailed PDF report.",
    )
