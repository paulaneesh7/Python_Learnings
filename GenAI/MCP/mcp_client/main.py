from __future__ import annotations
from fastmcp import FastMCP



mcp = FastMCP("arithmetic")


def _as_number(x):
    # Accept int/float or numeric string, raise clean errors otherwise
    if isinstance(x, (int, float)):
        return float(x)
    if isinstance(x, str):
        return float(x.strip())
    raise TypeError("Expected a number (int/float or numeric string)")



@mcp.tool()
async def add(a: float, b: float) -> float:
    """Return a + b.""" 
    return _as_number(a) + _as_number(b)


@mcp.tool()
async def subtract(a: float, b: float) -> float:
    """Return a - b."""
    return _as_number(a) - _as_number(b)


@mcp.tool()
async def multiply(a: float, b: float) -> float:
    """Return a * b."""
    return _as_number(a) * _as_number(b)


@mcp.tool()
async def divide(a: float, b: float) -> float:
    """Return a / b."""
    b = _as_number(b)
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return _as_number(a) / b



if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="127.0.0.1",
        port=8000,
        path="/mcp-server"
    )