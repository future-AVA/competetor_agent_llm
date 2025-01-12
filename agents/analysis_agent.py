from langchain.prompts import PromptTemplate
from langchain_groq.chat_models import ChatGroq

def perform_comparison_and_swot(company_data):
    """
    Perform SWOT analysis and compare companies.

    Args:
        company_data (str): Data about companies in plain text format.

    Returns:
        str: SWOT and comparison results in plain text.
    """
    # Initialize the language model
    language_model = ChatGroq(model="llama-3.2-1b-preview", temperature=0.7, max_tokens=2000)

    # Define the SWOT prompt
    swot_prompt = PromptTemplate(
        input_variables=["company_data"],
        template="""
        You are a business analyst specializing in SWOT and market comparisons.

        Based on the following company data:
        {company_data}

        Perform these tasks:
        1. Provide SWOT analysis (Strengths, Weaknesses, Opportunities, Threats) for each company.
        2. Compare companies based on funding, location, and technologies used.
        3. Recommend the top 3 companies with reasons.

        Present the results as plain text in the following format:
        SWOT Analysis:
        - Strengths:
        - Weaknesses:
        - Opportunities:
        - Threats:

        Comparison:
        - Summary of top 3 companies:
        """
    )

    # Generate SWOT and comparison results
    swot_results = language_model.invoke(swot_prompt.format(company_data=company_data))
    return swot_results.content if hasattr(swot_results, 'content') else str(swot_results)
