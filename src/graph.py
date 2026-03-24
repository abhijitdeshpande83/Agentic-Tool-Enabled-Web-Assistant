import os
from langchain_groq import ChatGroq
from tavily import TavilyClient
from rich import print
from typing import Annotated
from typing_extensions import TypedDict
from langchain_core.tools import tool
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
load_dotenv()

# Define Model
model="llama-3.3-70b-versatile"

# Define LLM
llm = ChatGroq(model=model)

# Define State
class State(TypedDict):

    messages: Annotated[list, add_messages]

# Define Tavily Tool

@tool
def search_web_tool(query:str):
    "Use this tool to search the internet for real-time information"
    tavily_search = TavilyClient()
    response = tavily_search.search(query=query)

    return [
        {'title':r.get('title','No Title available'),
         'content': r.get('content', 'No Content available'),
         'url': r.get('url','No url available')}
         for r in response.get('results',[])
    ]

# Tool bind with LLM
tools = [search_web_tool]
llm_with_tool = llm.bind_tools(tools)

# Node defincation
def tool_calling_llm(state:State):
    return {'messages':[llm_with_tool.invoke(state['messages'])]}


def build_graph():
    memory = MemorySaver()
    # Graph
    builder = StateGraph(State)
    # Add Nodes
    builder.add_node('tool_calling_llm', tool_calling_llm)
    builder.add_node('tools',ToolNode(tools))
    # Add Edges
    builder.add_edge(START,'tool_calling_llm')
    builder.add_conditional_edges(
        "tool_calling_llm",
        tools_condition
    )
    builder.add_edge('tools','tool_calling_llm')
    
    return builder.compile(checkpointer=memory)

agent = build_graph()
