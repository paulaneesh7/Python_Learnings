# Feedback 


from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv




load_dotenv()

model = ChatOpenAI(
    model="gpt-4.1"
)

parser = StrOutputParser()



class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')


parser2 = PydanticOutputParser(pydantic_object=Feedback)



prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}",
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)


classifier_chain = prompt1 | model | parser2

# Format of branch chain
# branch_chain = RunnableBranch(
#     (condition1, chain1),
#     (condition2, chain2),
#     default chain
# )



prompt2 = PromptTemplate(
    template="Write an appropriate response to this positive feedback \n {feedback}",
    input_variables=['feedback']
)


prompt3 = PromptTemplate(
    template="Write an appropriate response to this negative feedback \n {feedback}",
    input_variables=['feedback']
)



branch_chain = RunnableBranch(
    (lambda x : x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x : x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x : "Could not find sentiment")
)


chain = classifier_chain | branch_chain


result = chain.invoke({
    "feedback": "This is terrible phone"
})

print(result)



chain.get_graph().print_ascii()