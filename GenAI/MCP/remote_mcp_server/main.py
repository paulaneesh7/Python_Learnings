
from fastmcp import FastMCP
import random
import json

mcp = FastMCP(name="Simple Calculator Server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together.
    Args:
        a (int): The first number.
        b (int): The second number.
    Returns:
        int: The sum of the two numbers.
    """
    return a + b



@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract one number from another.
    Args:
        a (int): The first number.
        b (int): The second number.
    Returns:
        int: The difference of the two numbers.
    """
    return a - b



@mcp.tool()
def random_number(min_val: int = 1, max_val: int = 100) -> int:
    """Generate a random number between min_val and max_val.
    Args:
        min_val (int): The minimum value (inclusive).
        max_val (int): The maximum value (inclusive).
    Returns:
        int: A random number between min_val and max_val.
    """
    return random.randint(min_val, max_val)


@mcp.resource("info://server")
def server_info() -> str:
    """Get information about the server."""
    
    info = {
        "name": "Simple Calculator Server",
        "version": "1.0.0",
        "description": "A simple calculator server that can perform basic arithmetic operations and generate random numbers.",
        "tools": ["add", "subtrac", "random_numer"],
        "author": "Aneesh"
    }
    
    return json.dumps(info, indent=2)



if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)

