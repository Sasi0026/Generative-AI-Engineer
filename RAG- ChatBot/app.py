"""

A simple RAG (Retrieval-Augmented Generation) chatbot using LangGraph and LangChain,
which can answer conversational queries and also search the internet for up-to-date information
using the Tavily Search Engine tool.

Features:
- Conversational AI chatbot powered by a Groq-hosted Llama 3 model.
- Retrieval-augmented workflow: can extract and summarize content from internet sources.
- Modular state graph architecture with memory for context persistence.
- Integration of external tools for dynamic internet search and content extraction.

Requirements:
- langchain-core, langchain-community, langgraph, langchain-groq, requests, typing_extensions
- API keys for Groq and Tavily services

Author: [Sasi Kiran]

"""

import requests
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.checkpoint.memory import MemorySaver
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.graph import StateGraph, START, END
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.graph.message import add_messages
from langchain_core.messages import AIMessage, ToolMessage
import os

# ========================
# API KEY CONFIGURATION
# ========================
# Set your API keys for Groq (LLM provider) and Tavily (search tool) here.
# These should be securely loaded in production environments.
# groq_api_key = 'your_groq_api_key'
# tavily_key = 'your_tavily_api_key'
os.environ['GROQ_API_KEY'] = groq_api_key
os.environ['TAVILY_API_KEY'] = tavily_key

# ========================
# STATE DEFINITION
# ========================
class State(TypedDict):
    """
    State structure for the chatbot graph.
    Keeps track of the conversation history via the `messages` field.
    """
    messages: Annotated[list, add_messages]

# ========================
# GRAPH CONSTRUCTION
# ========================
# Create a LangGraph state graph object for workflow modeling.
graph_builder = StateGraph(State)

# ========================
# LLM AND TOOL BINDING
# ========================
# Initialize the conversational language model (Llama 3 via Groq API).
llm = ChatGroq(
    temperature=0.9,
    model_name="llama-3.1-8b-instant"
)

# Define and bind external tools (e.g., Tavily search engine) to the LLM.
# Tools must be defined; TavilySearchResults is used here for internet search.

tools = [TavilySearchResults()]
llm_with_tools = llm.bind_tools(tools=tools)

# ========================
# CHATBOT FUNCTION NODE
# ========================
def chatbot(state: State):
    """
    Main chatbot node.
    Receives the conversation state, invokes the LLM (with tools), and appends the response.
    """
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

# ========================
# GRAPH NODES AND EDGES
# ========================
# Add the chatbot node to the workflow graph.
graph_builder.add_node("chatbot", chatbot)

# Add the tool execution node.
tool_node = ToolNode(tools=tools)
graph_builder.add_node("tools", tool_node)

# Add conditional edges to route between chatbot and tools depending on workflow needs.
graph_builder.add_conditional_edges("chatbot", tools_condition)
graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge(START, "chatbot")

# ========================
# MEMORY AND GRAPH COMPILATION
# ========================
# Configure memory for context/history persistence.
memory = MemorySaver()
graph = graph_builder.compile(checkpointer=memory)

# ========================
# CHATBOT EXECUTION EXAMPLE
# ========================
# Example user prompt requesting recent research papers (demonstrates RAG workflow).

config = {"configurable": {"thread_id": "1"}}
user_input = (
    "Try to give the most recent research papers about humanoid robots, "
    "mostly released by Stanford, IIT Bombay, and Kharagpur. "
    "List more than 3 papers, only titles and the URLs."
)

# Stream the response from the chatbot graph.
# The config is passed as the second positional argument to stream().

events = graph.stream(
    {"messages": [("user", user_input)]},
    config,
    stream_mode="values"
)

# Print out chatbot responses as they are generated.
for event in events:
    event["messages"][-1].pretty_print()
