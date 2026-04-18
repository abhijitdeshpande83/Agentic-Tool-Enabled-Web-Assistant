# Agentic Tool-Enabled Web Assistant (ATLAS) 🚀

**ATLAS** is a LangGraph-powered autonomous AI agent that performs
real-time web research using Groq LLM and Tavily search.

------------------------------------------------------------------------

## Scope

Build a lightweight AI agent capable of performing **real-time web
research** while maintaining **session-based conversational context**.\
The agent uses **LangGraph orchestration** to dynamically decide when to
respond directly and when to invoke external tools.

------------------------------------------------------------------------

## Business Value

-   Demonstrates **tool-augmented LLM reasoning**
-   Enables **real-time knowledge retrieval**
-   Provides a **modular agent architecture**
-   Supports **serverless deployment** for scalable usage

------------------------------------------------------------------------

## 🛠 Tech Stack

<table>
  <tr>
    <td><strong>Agent Framework</strong></td>
    <td>
      <img src="https://img.shields.io/badge/LangGraph-000000?logo=langchain&logoColor=white" alt="LangGraph">
    </td>
  </tr>

  <tr>
    <td><strong>LLM Inference</strong></td>
    <td>
      <img src="https://img.shields.io/badge/Groq%20LLM-F55036?logo=groq&logoColor=white" alt="Groq LLM">
    </td>
  </tr>

  <tr>
    <td><strong>External Tools</strong></td>
    <td>
      <img src="https://img.shields.io/badge/Tavily%20Search-1E90FF?logo=googlechrome&logoColor=white" alt="Tavily">
    </td>
  </tr>

  <tr>
    <td><strong>Memory / State</strong></td>
    <td>
      <img src="https://img.shields.io/badge/LangGraph%20MemorySaver-000000?logo=langchain&logoColor=white" alt="MemorySaver">
    </td>
  </tr>

  <tr>
    <td><strong>Cloud / Deployment</strong></td>
    <td>
      <img src="https://img.shields.io/badge/AWS%20Lambda-FF9900?logo=awslambda&logoColor=white" alt="Lambda">
      <img src="https://img.shields.io/badge/API%20Gateway-FF4F8B?logo=amazonaws&logoColor=white" alt="API Gateway">
      <img src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white" alt="Docker">
    </td>
  </tr>

  <tr>
    <td><strong>Programming Language</strong></td>
    <td>
      <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python">
    </td>
  </tr>
</table>

------------------------------------------------------------------------

## Architecture
<h2>Process flow Diagram</h2>
<p align="center">
    <img src="docs/Taskpilot-process-flow.png" alt="Process flow"/>
</p>
<h2>Graph</h2>
<p align="center">
    <img src="docs/graph.png" alt="Graph" />
</p>

------------------------------------------------------------------------

## Implementation

-   Built an **agentic workflow using LangGraph** for reasoning and tool
    orchestration.
-   Integrated **Groq LLM** for fast, low-latency inference.
-   Added **Tavily Search** for real-time web information retrieval.
-   Implemented **MemorySaver checkpointing** for session-based memory.
-   Organized code into **modular components** for agent logic and
    tools.
-   Containerized the project using **Docker**.
-   Added **AWS Lambda Function** with JSON parsing and CORS support for
    API Gateway.

------------------------------------------------------------------------

## Challenges

- **CORS with API Gateway:** Direct frontend requests to API Gateway failed due to CORS restrictions. The solution was to route requests through the **Django backend**, which calls the Lambda endpoint and returns the response to the frontend.

- **Agent Workflow Structure:** Understanding how to **separate agent definition from execution** in LangGraph and invoking it through a `run_agent` function required careful design initially.

------------------------------------------------------------------------

## Outcome

A lightweight LangGraph-based agent capable of **real-time web research,
tool usage, and contextual conversations**, deployable locally or in
serverless environments.
