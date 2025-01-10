from langgraph import LangGraph, Node
from memory_manager import MemoryManager
from research_agent import research_agent_function
from analysis_agent import analysis_agent_function
from visualization_agent import visualization_agent_function
from report_agent import report_generation_agent_function

# Initialize LangGraph and Memory
graph = LangGraph()
memory = MemoryManager()

#research agent (aggregate data from different websites)
def research_node(context):
    topic = context["topic"]
    research_data = research_agent_function(topic)
    memory.store("research_data", research_data)
    return {"research_data": research_data}
# analysis agent(COMPARISON &SWOT ANALYSIS)
def analysis_node(context):
    research_data = memory.retrieve("research_data")
    analysis_result = analysis_agent_function(research_data)
    memory.store("analysis_result", analysis_result)
    return {"analysis_result": analysis_result}
# Visualization Agent
def visualization_node(context):
    analysis_result = memory.retrieve("analysis_result")
    visualization_output = visualization_agent_function(analysis_result)
    memory.store("visualization_output", visualization_output)
    return {"visualization_output": visualization_output}
# Report Agent
def report_node(context):
    research_data = memory.retrieve("research_data")
    analysis_result = memory.retrieve("analysis_result")
    visualization_output = memory.retrieve("visualization_output")
    return report_generation_agent_function(research_data, analysis_result, visualization_output)

# Build graph
graph.add_node(Node("research", research_node))
graph.add_node(Node("analysis", analysis_node, dependencies=["research"]))
graph.add_node(Node("visualization", visualization_node, dependencies=["analysis"]))
graph.add_node(Node("report", report_node, dependencies=["visualization"]))

def orchestrate(topic):
    context = {"topic": topic}
    return graph.run(context)["report"]
