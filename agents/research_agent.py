import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_groq.chat_models import ChatGroq

load_dotenv()

def aggregate_data(query):
    """
    Collect data on AI startups based on the input query.

    Args:
        query (str): The search query (e.g., "AI startups in healthcare").

    Returns:
        str: Aggregated plain-text data.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY is not set in the environment variables.")

    # Initialize the language model
    language_model = ChatGroq(model="llama-3.2-1b-preview", temperature=0.7, max_tokens=2000)

    # Define the research prompt
    research_prompt = PromptTemplate(
        input_variables=["query"],
        template="""
        You are a researcher gathering detailed information about AI startups in the given sector.

        Query: {query}

        Collect details about 5-10 companies:
        - Name
        - Location
        - Funding information
        - Technologies used
        - Resources provided

        Present the output as plain text in the following format:
        Company Name: <Name>
        Location: <Location>
        Funding: <Funding Amount>
        Technologies: <Technologies>
        Resources: <Resources>

        Separate each company’s information with a blank line.
        """
    )

    # Fetch aggregated data
    response = language_model.invoke(research_prompt.format(query=query))
    return response.content if hasattr(response, 'content') else str(response)
