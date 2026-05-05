from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()



prompt1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)


prompt2 = PromptTemplate(
    template="Explain the following joke: {joke}",
    input_variables=["joke"]
)


model = ChatOpenAI(
    model="gpt-4.1"
)

parser = StrOutputParser()


chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)


result = chain.invoke({
    "topic": "AI"
})

print(result)