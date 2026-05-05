from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableLambda
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()

model = ChatOpenAI(
    model="gpt-4.1"
)

parser = StrOutputParser()



short_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in 1-2 lines"
)


detailed_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in details"
)





chain = RunnableParallel({
    "short": RunnableLambda(lambda x: x ['short']) | short_prompt | model | parser,
    "detailed": RunnableLambda(lambda x : x ['detailed']) | detailed_prompt | model | parser,
})


result = chain.invoke({
    "short": {
        "topic": "Machine Learning"
    },
    "detailed": {
        "topic": "Deep Learning"
    }
})


print(f"Result Short: {result["short"]}")
print(f"\nResult Detailed: {result["detailed"]}")

