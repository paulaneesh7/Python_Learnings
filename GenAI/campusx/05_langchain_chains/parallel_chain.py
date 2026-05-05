# Merge notes and quiz into 1 chain

from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv



load_dotenv()

model1 = ChatOpenAI(
    model="gpt-4.1"
)

model2 = ChatMistralAI(
    model="mistral-small-2506",
)

parser = StrOutputParser()


text = """

AI memory or AI agent memory is an agent's ability to retain and recall relevant information across time, tasks, and multiple user interactions. Memory allows AI agents to remember what happened in the past and use that information to improve behavior in the future.

Memory is not about storing just the chat history or pumping more tokens into the prompt. It’s about building a persistent internal state that evolves and informs every interaction the agent has, even weeks or months apart.

Three pillars define memory in agents:

State: Knowing what’s happening right now

Persistence: Retaining knowledge across sessions

Selection: Deciding what’s worth remembering

Together, these enable something we’ve never had before: continuity.

"""



prompt1 = PromptTemplate(
    template="Generate short and simple notes from the following text \n {text}",
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template="Generate 5 short question answers from the following text \n {text}",
    input_variables=['text']
)

final_prompt = PromptTemplate(
    template="Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}",
    input_variables=['notes', 'quiz']
)



# Parallel chain execution
parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})


# Merging chain
merge_chain = final_prompt | model1 | parser


# Connect both the chains
chain = parallel_chain | merge_chain


result = chain.invoke({
    'text': text
})

print("\n" + result)