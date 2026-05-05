import os
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()
os.environ["USER_AGENT"] = "Mozilla/5.0"

model = ChatOpenAI()

prompt = PromptTemplate(
    template='Answer the following question:\n{question}\n\nFrom this text:\n{text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

URL = "https://en.wikipedia.org/wiki/Artificial_intelligence"

loader = WebBaseLoader(URL)
docs = loader.load()

text = docs[0].page_content[:3000]

chain = prompt | model | parser

result = chain.invoke({
    "question": "What is Artificial Intelligence?",
    "text": text
})

print(result)