from langgraph.graph import StateGraph, START, END
from graph.state import GraphState
from graph.nodes import (
    clarification_node,
    answer_node,
    clarity_checker_node
)



def build_graph():
    builder = StateGraph(GraphState)
    
    
    
    builder.add_node("clarity_checker", clarity_checker_node)
    builder.add_node("answer", answer_node)
    builder.add_node("clarification", clarification_node)
    
    
    builder.set_entry_point("clarity_checker")
    
    
    def route_based_on_clarity(state: GraphState):
        if state["is_clear"]:
            return "answer"
        else:
            return "clarification"
    
    builder.add_conditional_edges(
        "clarity_checker",
        route_based_on_clarity,
        {
            "answer": "answer",
            "clarification": "clarification"
        }
    )
    
    
    # Edges
    builder.add_edge("answer", END)
    builder.add_edge("clarification", END)
    
    
    return builder.compile()
    