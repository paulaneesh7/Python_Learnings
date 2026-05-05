from typing import TypedDict, List, Optional


class GraphState(TypedDict):
    user_query: str
    is_clear: Optional[bool]
    clarification_question: Optional[str]
    final_answer: Optional[str]
    chat_history: List[str]
    
    
    
    
"""
For Smart Q&A with clarifications we need:

user input
whether it's clear
generated answer
clarification question
conversation history (for later memory use)

"""
