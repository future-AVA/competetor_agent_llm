from langchain.prompts import PromptTemplate
from langchain_groq.chat_models import ChatGroq
from dotenv import load_dotenv

load_dotenv()

def aggregate_data(query):
    """
    Collect data on AI startups based on the input query.

    Args:
        query (str): The search query (e.g., "AI startups in healthcare").

    Returns:
        str: Aggregated plain-text data.
    """
    language_model = ChatGroq(model="llama-3.2-1b-preview", temperature=0.7, max_tokens=2000)

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

    response = language_model.invoke(research_prompt.format(query=query))
    return response.content if hasattr(response, 'content') else str(response)
