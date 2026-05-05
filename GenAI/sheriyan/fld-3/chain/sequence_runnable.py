from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()



prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words"
)


model = ChatOpenAI(
    model="gpt-4.1"
)

parser = StrOutputParser()


formatted_prompt = prompt.invoke(
    {"topic": "Machine Learning"}
)


response = model.invoke(formatted_prompt)

result = parser.parse(response.content)

print("Final output: ", result)


"""

Modern way to use Chain: Through runnable
Code below:
"""


chain = prompt | model | parser

res = chain.invoke({
    "topic": "Machine Learning"
})

print("Response from runnable chain: ", res)