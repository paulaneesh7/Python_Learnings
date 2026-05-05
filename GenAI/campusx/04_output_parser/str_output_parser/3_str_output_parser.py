# This code is same as 2_str_output_parser but 
# without long usage of chain


from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()


model = ChatOpenAI(
    model="gpt-4.1",
    temperature=0.7
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

parser = StrOutputParser()


report = (template1 | model | parser).invoke({
    'topic': 'black hole'
})

summary = (template2 | model | parser).invoke({
    'text': report
})

print(f"\nSummary: {summary}")


# Without using any chain
PROMPT = """
What is the capital of India and write 5 line summary about it
"""

response = model.invoke(PROMPT)

result = parser.invoke(response)

print("\n" + result)