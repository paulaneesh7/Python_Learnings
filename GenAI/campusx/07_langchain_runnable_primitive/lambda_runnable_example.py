from langchain_core.runnables import RunnableLambda


def word_counter(text: str) -> int:
    return len(text.split())


if __name__ == "__main__":
    
    runnable_word_counter = RunnableLambda(word_counter)


    result = runnable_word_counter.invoke("Hello world! This is a test.")  # Output: 6

    print(result)