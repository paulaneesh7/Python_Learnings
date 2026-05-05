from graph.state import GraphState


def clarity_checker_node(state: GraphState) -> GraphState:
    query = state['user_query']
    
    
    # If query is too short -> unclear
    if len(query.split()) < 3:
        is_clear = False
    else:
        is_clear = True
        
    return {
        **state,
        "is_clear": is_clear
    }
    
    
def answer_node(state: GraphState) -> GraphState:
    query = state['user_query']
    
    answer = f"Answer to {query}"
    
    return {
        **state,
        "final_answer": answer
    }
    
    
    

def clarification_node(state: GraphState) -> GraphState:
    query = state['user_query']
    
    clarification = f"Can you clarify what you mean by {query}?"
    
    
    return {
        **state,
        "clarification_question": clarification
    }