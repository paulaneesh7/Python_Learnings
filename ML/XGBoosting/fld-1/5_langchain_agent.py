from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.tools import tool

from titanic_tool import titanic_survival_predictor

llm = ChatOpenAI()

tools = [titanic_survival_predictor]

agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True
)

agent.run("""
Predict survival for:
Pclass=1, Sex=female, Age=30, SibSp=0, Parch=0, Fare=100, Embarked=C
""")