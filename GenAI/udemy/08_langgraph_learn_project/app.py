from graph.graph_builder import build_graph


graph = build_graph()


initial_state = {
    "user_query": "Database?",
    "is_clear": None,
    "clarification_question": None,
    "final_answer": None,
    "chat_history": []
}


while True:
    user_input = input("\nYou: ")
    
    if user_input.lower() in ["exit", "quit"]:
        break
    
    
    initial_state["user_query"] = user_input
    initial_state["is_clear"] = None
    initial_state["clarification_question"] = None
    initial_state["final_answer"] = None
    
    
    
    result = graph.invoke(initial_state)
    
    
    if result["is_clear"] is False:
        print("\nAgent: ", result["clarification_question"])
    else:
        print("\nAgent: ", result["final_answer"])
        
        
    state = result