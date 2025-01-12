import os
import pandas as pd
import matplotlib.pyplot as plt

def generate_visualizations(company_data):
    """
    Generate visualizations for company comparison data.

    Args:
        company_data (str): Plain-text company data.

    Returns:
        list: Paths to saved visualization images.
    """
    companies = []
    for block in company_data.strip().split("\n\n"):
        company = {}
        for line in block.split("\n"):
            line = line.strip()
            if line.startswith("Company Name:"):
                company["Company"] = line.split(":", 1)[1].strip()
            elif line.startswith("Funding:"):
                try:
                    company["Funding"] = int(line.split(":", 1)[1].strip().replace(",", ""))
                except ValueError:
                    company["Funding"] = 0
        if company.get("Company"):
            companies.append(company)

    df = pd.DataFrame(companies)

    if df.empty:
        print("No valid data for visualization.")
        return []

    visualization_dir = "visualizations"
    os.makedirs(visualization_dir, exist_ok=True)

    image_paths = []

    if "Funding" in df.columns:
        funding_chart_path = os.path.join(visualization_dir, "funding_comparison.png")
        df.plot(x="Company", y="Funding", kind="bar", title="Funding Comparison")
        plt.savefig(funding_chart_path)
        image_paths.append(funding_chart_path)

    return image_paths
