from pydantic import BaseModel
from typing import List

#setup pydantic model

class RequestState(BaseModel):
    system_prompt: str
    messages: List[str]
    allow_search: bool

#setup ai agents from frontend request
from fastapi import FastAPI
from ai_agent import aiagent
app=FastAPI(title="AI Agent")
@app.post("/chat")

def chat_endpoint(request:RequestState):
    """
    API endpoint to interact with chatbot using langgraph and search tools.
    """
    query=request.messages
    allowsearch=request.allow_search
    #systemprompt=request.system_prompt
    #response=aiagent(systemprompt, query, allowsearch)
    response=aiagent(query, allowsearch)
    return response

#for local developement only
# import uvicorn
# if __name__=="__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9999)
