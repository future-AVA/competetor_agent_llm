from langchain.prompts import PromptTemplate
from langchain_groq.chat_models import ChatGroq

def perform_comparison_and_swot(company_data):
    """
    Perform SWOT analysis and compare companies.

    Args:
        company_data (str): Data about companies in plain text format.

    Returns:
        str: SWOT and comparison results in structured plain text.
    """
    language_model = ChatGroq(model="llama-3.2-1b-preview", temperature=0.7, max_tokens=2000)

    swot_prompt = PromptTemplate(
        input_variables=["company_data"],
        template="""
        You are a business analyst specializing in SWOT analysis and market comparisons.

        Based on the following company data:
        {company_data}

        Perform these tasks:
        1. Provide SWOT analysis (Strengths, Weaknesses, Opportunities, Threats) for each company.
        2. Rank the companies based on their strengths, opportunities, and overall potential.
        3. Suggest the top 3 companies with reasons.

        Provide the output in this structured format:

        Company: <Company Name>
        Strengths: <List of strengths>
        Weaknesses: <List of weaknesses>
        Opportunities: <List of opportunities>
        Threats: <List of threats>

        Top Companies:
        1. <Top Company 1> - <Reason>
        2. <Top Company 2> - <Reason>
        3. <Top Company 3> - <Reason>
        """
    )

    swot_results = language_model.invoke(swot_prompt.format(company_data=company_data))
    return swot_results.content if hasattr(swot_results, 'content') else str(swot_results)
