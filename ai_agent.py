#import libraries
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

load_dotenv()

#import environments
#for localhost (development)
# os.environ['GROQ_API_KEY']=os.getenv("GROQ_API_KEY")
# os.environ['TAVILY_API_KEY']=os.getenv("TAVILY_API_KEY")

#for production (hosting in render)
GROQ_API_KEY=os.getenv("GROQ_API_KEY")
TAVILY_API_KEY=os.getenv("TAVILY_API_KEY")

#initialize model and agent
systemprompt="AI chatbot"

#def aiagent(system_prompt, query, allowsearch):
def aiagent(prompt, query, allowsearch):
    llm=ChatGroq(model="llama-3.3-70b-versatile")
    tools=[TavilySearchResults(max_results=2)] if allowsearch else []

    #agent=create_react_agent(model=llm,tools=tools,state_modifier=systemprompt)
    agent=create_react_agent(model=llm,tools=tools,prompt=systemprompt)
    state={'messages':query}
    response=agent.invoke(state)
    messages=response.get("messages")
    aimsg=[message.content for message in messages if isinstance(message,AIMessage)]
    return (aimsg[-1])

