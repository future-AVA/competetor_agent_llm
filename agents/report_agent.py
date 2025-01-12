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

def generate_pdf_report(research_data, analysis_data, visualization_path):
    """
    Generate a PDF report.

    Args:
        research_data (str): Research data.
        analysis_data (str): Analysis results.
        visualization_path (str): Path to visualization.

    Returns:
        str: Path to the generated PDF report.
    """
    pdf = PDFReport()
    pdf.add_page()
    pdf.add_section("Executive Summary", "Generated using a shared LLaMA-based model.")
    pdf.add_section("Research Data", research_data)
    pdf.add_section("SWOT Analysis", analysis_data)
    pdf.image(visualization_path, x=10, y=None, w=180)

    output_path = "generated_reports/AI_Startup_Report.pdf"
    pdf.output(output_path)
    return output_path
