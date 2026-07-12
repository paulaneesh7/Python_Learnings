from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
import os
os.environ['OPENAI_API_KEY'] = 'test'
agent = create_agent(model=ChatOpenAI(openai_api_key='test'), tools=[DuckDuckGoSearchRun()], system_prompt='You are helpful.')
print(type(agent))
print([m for m in dir(agent) if not m.startswith('_')])
print('has_invoke', hasattr(agent,'invoke'))
print('has_run', hasattr(agent,'run'))
print('has_stream', hasattr(agent,'stream'))
