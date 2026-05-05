from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from lambda_runnable_example import word_counter

load_dotenv()

model = ChatOpenAI(
    model="gpt-4.1"
)


parser = StrOutputParser()





prompt = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)


prompt2 = PromptTemplate(
    template="Explain the following joke: {joke}",
    input_variables=["joke"]
)


joke_generator_chain = RunnableSequence(prompt, model, parser)


parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_counter)
})



final_chain = RunnableSequence(joke_generator_chain, parallel_chain)



result = final_chain.invoke({
    "topic": "cricket"
})


print("🤣 Joke:", result['joke'])
print("📊 Word Count:", result['word_count'])