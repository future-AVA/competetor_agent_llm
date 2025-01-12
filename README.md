# **🔎 AI Startup Analysis Tool**

This project provides an end-to-end solution for analyzing AI startups and generating comprehensive reports, including SWOT analysis and visualizations. The project is structured into four agents, orchestrated to work together seamlessly.

---

## **Features**
- **Data Aggregation**: The research agent aggregates data from multiple sources.
- **SWOT Analysis**: The analysis agent performs a detailed SWOT and sentiment analysis.
- **Visualization**: The visualization agent generates insightful charts.
- **Report Generation**: The report agent compiles findings into a structured PDF report.

---

## **Project Structure**


<img src="https://github.com/future-AVA/competetor_agent_llm/blob/main/assets/chatbot%20-%20Page%204.png" alt="Logo" width="1000">

## Introduction
This is a description of the project.

### **Agents**
1. **Research Agent**:
   - Aggregates data and summarizes it for further analysis.
   - Tool: `DuckDuckGoSearchTool`.

2. **Analysis Agent**:
   - Performs SWOT and sentiment analysis on aggregated data.

3. **Visualization Agent**:
   - Processes analysis results and generates visualizations (e.g., bar charts).

4. **Report Agent**:
   - Combines all results into a structured, downloadable PDF report.

### **Orchestrator**
The orchestrator coordinates all agents to execute the workflow in the following sequence:
1. Aggregate data using the research agent.
2. Perform SWOT and sentiment analysis using the analysis agent.
3. Generate visualizations using the visualization agent.
4. Compile a PDF report using the report agent.

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/ai-startup-analysis.git

cd ai-startup-analysis
```
### **2. Install Dependencies**
Install the required Python libraries:
```
pip install - requirements.txt
```

### **3. Run the Application**
Launch the Gradio interface:
```
python gradio_interface.py
```
### **4. Access the Interface**
Open the provided URL in your browser (e.g., http://127.0.0.1:7860) to interact with the application.

### **Usage**
Enter the topic for analysis in the Gradio interface.
Example: "AI startups in healthcare from 2020-2025".
Click the "Submit" button to start the workflow.
Download the generated PDF report.
## Technical Overview
Core Scripts
- hf_api_model.py: Loads and initializes the shared Hugging Face model for CPU inference.
- research_agent.py: Implements the research agent to aggregate data.
- analysis_agent.py: Implements the analysis agent to perform SWOT and sentiment analysis.
- visualization_agent.py: Implements the visualization agent for generating charts.
- report_agent.py: Implements the report agent to compile results into a PDF.
- orchestrator.py: Coordinates all agents to execute the workflow.
- gradio_interface.py: Provides a Gradio-based user interface.
## Model
The application uses the groq llama 3.2 1b preview model. The model is loaded with optimizations for CPU inference and low memory usage.

## Directory Structure
```
├── agents/
│   ├── research_agent.py       # Research agent
│   ├── analysis_agent.py       # Analysis agent
│   ├── visualization_agent.py  # Visualization agent
│   ├── report_agent.py         # Report agent
├── orchestrator.py             # Orchestrator for workflow execution
├── hf_api_model.py             # Shared model loader
├── gradio_interface.py         # Gradio interface for the app
├── generated_reports/          # Directory for generated PDF reports
└── README.md                   # Project documentation

```

## Example .env File:
```
GROQ_API_KEY:
HF_API_TOKEN:
JINA_API_KEY:
```

.


## Example Workflow
**Input:**
Topic: "AI startups in healthcare from 2020-2025".
## Workflow:
- The research agent aggregates data about the startups.
- The analysis agent identifies strengths, weaknesses, opportunities, and threats (SWOT).
- The visualization agent creates charts for SWOT results.
- The report agent compiles all data into a PDF report.



**Output:**
A downloadable PDF report with detailed findings.
