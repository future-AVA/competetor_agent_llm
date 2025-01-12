from fpdf import FPDF

class PDFReport(FPDF):
    """
    Generates a professional PDF report with plain text, visualizations, and tables.
    """
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'AI Startup Analysis Report', align='C', ln=1)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def add_section(self, title, content):
        """
        Adds a section to the PDF.

        Args:
            title (str): The section title.
            content (str): The section content.
        """
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, ln=1)
        self.set_font('Arial', '', 11)
        if isinstance(content, str):
            self.multi_cell(0, 10, content)
        else:
            self.multi_cell(0, 10, str(content))
        self.ln()

    def add_visualizations(self, image_paths):
        """
        Adds visualizations to the PDF.

        Args:
            image_paths (list): List of paths to visualization images.
        """
        for image_path in image_paths:
            self.add_page()
            self.image(image_path, x=10, y=None, w=180)

def generate_report(company_data, swot_results, visualizations):
    """
    Generate a PDF report with plain text, tables, and visualizations.

    Args:
        company_data (str): Company data summary in plain text.
        swot_results (str): SWOT and comparison results in plain text.
        visualizations (list): Paths to visualization images (can be empty).

    Returns:
        str: Path to the generated PDF report.
    """
    pdf = PDFReport()
    pdf.add_page()

    # Add sections
    pdf.add_section("Executive Summary", "AI startup analysis in healthcare.")
    pdf.add_section("Company Data", company_data)
    pdf.add_section("SWOT and Comparison Results", swot_results)

    # Add visualizations or fallback message
    if visualizations:
        pdf.add_visualizations(visualizations)
    else:
        pdf.add_section("Visualizations", "No valid data available for generating visualizations.")

    output_path = "AI_Startup_Report.pdf"
    pdf.output(output_path)
    return output_path
