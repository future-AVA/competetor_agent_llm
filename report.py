from hf_api_model import HfApiModel

def report_generation_agent_function(research_data, analysis_result, visualization_output):
    """Compiles a detailed report."""
    model = HfApiModel(model_id="meta-llama/Llama-2-7b-chat-hf")  # Report generation model
    prompt = f"""
    Create a detailed professional report for AI startups in {research_data['topic']}:
    - **Research Data**: {research_data['data']}
    - **SWOT Analysis**: {analysis_result['swot']}
    - **Sentiment Insights**: {analysis_result['sentiment']}
    Include the following visualization: {visualization_output['visualization']}.
    """
    report = model.run(prompt)
    return {"report": report}
