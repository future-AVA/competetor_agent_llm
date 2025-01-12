import os
import pandas as pd
import matplotlib.pyplot as plt

def generate_visualizations(company_data):
    """
    Generate visualizations for company comparison data.

    Args:
        company_data (str): Plain-text company data.

    Returns:
        list: Paths to saved visualization images (or an empty list if no valid data).
    """
    companies = []

    # Split company data into blocks by blank lines
    for block in company_data.strip().split("\n\n"):
        company = {}
        for line in block.split("\n"):
            line = line.strip()
            if line.startswith("Company Name:"):
                company["Company"] = line.split(":", 1)[1].strip()
            elif line.startswith("Location:"):
                company["Location"] = line.split(":", 1)[1].strip()
            elif line.startswith("Funding:"):
                try:
                    company["Funding"] = int(line.split(":", 1)[1].strip().replace(",", ""))
                except ValueError:
                    company["Funding"] = None  # Leave funding as None if parsing fails
        if company.get("Company"):  # Only include companies with a valid name
            companies.append(company)

    # Convert to DataFrame
    df = pd.DataFrame(companies)

    # If no valid data is available, return an empty list
    if df.empty:
        print("No valid company data for visualization.")
        return []

    # Create a directory for visualizations
    visualization_dir = "visualizations"
    os.makedirs(visualization_dir, exist_ok=True)

    image_paths = []

    # Generate funding comparison chart if Funding column exists
    if "Funding" in df.columns and df["Funding"].notna().any():
        funding_chart_path = os.path.join(visualization_dir, "funding_comparison.png")
        plt.figure(figsize=(10, 6))
        df.plot(x="Company", y="Funding", kind="bar", title="Funding Comparison")
        plt.savefig(funding_chart_path)
        image_paths.append(funding_chart_path)

    # Generate location distribution chart if Location column exists
    if "Location" in df.columns and df["Location"].notna().any():
        location_chart_path = os.path.join(visualization_dir, "location_distribution.png")
        location_counts = df["Location"].value_counts()
        location_counts.plot(kind="pie", autopct='%1.1f%%', title="Location Distribution")
        plt.savefig(location_chart_path)
        image_paths.append(location_chart_path)

    return image_paths
