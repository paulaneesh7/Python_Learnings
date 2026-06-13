import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import ToolMessage


load_dotenv()



SERVERS = {
    "LOCAL_URL": "http://localhost:8000/mcp-server/",
    "REMOTE_URL": "https://round-magenta-gerbil.fastmcp.app/"
}



llm = ChatOpenAI(
    model="gpt-5"
)



async def get_tools() -> list:
    """Connect to the MCP server and return tools as a list."""    
    
    client1 = MultiServerMCPClient({
        "Arithmetic": {
            "url": SERVERS["LOCAL_URL"],
            "transport": "streamable-http",
            "timeout": 300
        }
    })
    
    
    client2 = MultiServerMCPClient({
        "ExpenseTracker": {
            "url": SERVERS["REMOTE_URL"],
            "transport": "http",
            "timeout": 300
        }
    })
    
    
    return await client1.get_tools()

    



async def main():
    tools = await get_tools()
    
    named_tools = {}
    for tool in tools:
        named_tools[tool.name] = tool
    
    
    llm_with_tools = llm.bind_tools(tools)
    
    prompt = """
        Use the multiply tool to calculate the product of 12 and 15.
        Do not solve it yourself.
    """
    
    # prompt = """
    #     What is the product of 12 and 15 using the math tool?
    # """
    
    # LLM Response with tool calls
    response = await llm_with_tools.ainvoke(prompt)
    
    # Check if the LLM's response contains any tool calls, if not then print the LLM's response and return
    if not getattr(response, "tool_calls", None):
        print("\nLLM Reply:", response.content)
        return
    
    
    
    # If the LLM's response contains tool calls, invoke the tools and collect their results
    tool_message = []
    for tc in response.tool_calls:
        selected_tool = tc["name"]
        selected_tool_args = tc["args"]
        selected_tool_id = tc["id"]
        
        # Invoke the selected tool with the provided arguments and collect the result
        tool_result = await named_tools[selected_tool].ainvoke(selected_tool_args)
        
        # Append the tool's result to the tool_message list
        tool_message.append(ToolMessage(content=tool_result, tool_call_id=selected_tool_id))
    
    
    # Generate the final response from the LLM using the original prompt, the LLM's response, and the tool's result
    final_response = await llm_with_tools.ainvoke(
        [prompt, response, tool_message]
    )
    
    print(f"Final Response: {final_response.content}")
    
    
if __name__ == "__main__":
    asyncio.run(main())
    
    
    
"""
Check vid: 26:48 mins
"""
