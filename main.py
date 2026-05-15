import requests
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
import os
load_dotenv()

@tool("get_weather",description="returns weather for given city.")
def get_weather(city:str):
    response=requests.get(f'https://wttr.in/{city}?format=j1')
    return response.json()

llm=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)
agent=create_agent( 
    model=llm,
    tools=[get_weather],
    system_prompt="You are a helpful weather assistent that presents weather like a sarcastic TV anchor."
)
response=agent.invoke(
{    
 "messages": [
        {"role": "user", "content": "what is the weather in lahore"}
    ]
 })
print(response['messages'][-1].content)