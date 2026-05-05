from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model1 = ChatHuggingFace(
    llm=llm
)


model = ChatOpenAI(
    model="gpt-4.1",
    temperature=0.7,
)


# 1st prompt => detailed report
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic'],
    validate_template=True
)


# 2nd prompt => summary

template2 = PromptTemplate(
    template="Write a 5 line summary on the following text. \n {text}",
    input_variables=['text'],
    validate_template=True
)


prompt1 = template1.invoke({
    'topic': 'black hole'
})

result1 = model.invoke(prompt1)


prompt2 = template2.invoke({
    'text': result1.content
})

result2 = model.invoke(prompt2)


print(result2.content)