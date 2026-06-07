from fastmcp import FastMCP
import os
import sqlite3
import json


DB_PATH = os.path.join(os.path.dirname(__file__), "expense.db")
CATEGORIES_PATH = os.path.join(os.path.dirname(__file__), "categories.json")

mcp = FastMCP(name="ExpenseTracker")

def init_db():
    """Initialize the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            subcategory TEXT default '',
            note TEXT DEFAULT ''
        )
    """)
    conn.commit()
    conn.close()
    

init_db()


@mcp.tool()
def add_expense(amount: float, category: str, date: str, subcategory: str = "", note: str = "") -> str:
    """Add an expense to the database and return the expense ID."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO expenses (amount, category, date, subcategory, note)
        VALUES (?, ?, ?, ?, ?)
    """, (amount, category, date, subcategory, note))
    conn.commit()
    expense_id = cursor.lastrowid
    conn.close()
    return json.dumps({
        "status": "ok",
        "id": expense_id
    })


@mcp.tool()
def list_all_expenses() -> list[dict]:
    """List all expenses in the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, amount, category, date, subcategory, note FROM expenses")
    rows = cursor.fetchall()
    conn.close()
    return [
        {
            "id": row[0],
            "amount": row[1],
            "category": row[2],
            "date": row[3],
            "subcategory": row[4],
            "note": row[5]
        }
        for row in rows
    ]
    
    
    
@mcp.tool()
def list_expense_within_date(start_date: str, end_date: str) -> list[dict]:
    """List expense withing a date range."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
            SELECT id, date, amount, category, subcategory, note
            FROM expenses
            WHERE date BETWEEN ? AND ?
            ORDER BY id ASC
        """,
        (start_date, end_date)
    )
    rows = cursor.fetchall()
    conn.close()
    
    return [
        {
            "id": row[0],
            "date": row[1],
            "amount": row[2],
            "category": row[3],
            "subcategory": row[4],
            "note": row[5]
        }
        for row in rows
    ]

@mcp.tool()
def delete_all_expenses()-> dict:
    """Delete all expenses from the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses")
    conn.commit()
    conn.close()
    
    return {
        "status": "ok",
        "message": "All expenses have been deleted."
    }




@mcp.tool()
def summarize(start_date: str, end_date: str, category=None) -> dict:
    """Summarize expenses within a date range, optionally filtered by category."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    if category:
        cursor.execute(
            """
                SELECT category, SUM(amount) as total
                FROM expenses
                WHERE date BETWEEN ? AND ? AND category = ?
                GROUP BY category
            """,
            (start_date, end_date, category)
        )
    else:
        cursor.execute(
            """
                SELECT category, SUM(amount) as total
                FROM expenses
                WHERE date BETWEEN ? AND ?
                GROUP BY category
            """,
            (start_date, end_date)
        )
    
    rows = cursor.fetchall()
    conn.close()
    
    return {
        "summary": [
            {
                "category": row[0],
                "total": row[1]
            }
            for row in rows
        ]
    }


@mcp.resource("expense://categories", mime_type="application/json")
def categories():
    
    # Read fresh each time so you can edit the file without restarting
    with open(CATEGORIES_PATH, "r", encoding="utf-8") as f:
        return f.read()



if __name__ == "__main__":
    mcp.run()