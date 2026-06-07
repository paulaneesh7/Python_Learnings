from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import os
import sqlite3
import json

app = FastAPI(title="Expense Tracker API")

DB_PATH = os.path.join(os.path.dirname(__file__), "expense.db")
CATEGORIES_PATH = os.path.join(os.path.dirname(__file__), "categories.json")


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            subcategory TEXT DEFAULT '',
            note TEXT DEFAULT ''
        )
    """)

    conn.commit()
    conn.close()


    init_db()


class ExpenseCreate(BaseModel):
    amount: float
    category: str
    date: str
    subcategory: Optional[str] = ""
    note: Optional[str] = ""

class SummaryRequest(BaseModel):
    start_date: str
    end_date: str
    category: Optional[str] = None


@app.post("/expenses/add")
def add_expense(expense: ExpenseCreate):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO expenses (amount, category, date, subcategory, note)
        VALUES (?, ?, ?, ?, ?)
    """, (
        expense.amount,
        expense.category,
        expense.date,
        expense.subcategory,
        expense.note
    ))

    conn.commit()

    expense_id = cursor.lastrowid

    conn.close()

    return {
        "status": "ok",
        "id": expense_id
    }


@app.get("/expenses")
def list_all_expenses():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, amount, category, date, subcategory, note
        FROM expenses
    """)

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


@app.get("/expenses/range")
def list_expense_within_date(start_date: str, end_date: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, date, amount, category, subcategory, note
        FROM expenses
        WHERE date BETWEEN ? AND ?
        ORDER BY id ASC
    """, (start_date, end_date))

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


@app.delete("/expenses")
def delete_all_expenses():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses")

    conn.commit()
    conn.close()

    return {
        "status": "ok",
        "message": "All expenses have been deleted."
    }


@app.post("/expenses/summary")
def summarize(summary_request: SummaryRequest):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    if summary_request.category:

        cursor.execute("""
            SELECT category, SUM(amount) as total
            FROM expenses
            WHERE date BETWEEN ? AND ?
            AND category = ?
            GROUP BY category
        """, (
            summary_request.start_date,
            summary_request.end_date,
            summary_request.category
        ))

    else:

        cursor.execute("""
            SELECT category, SUM(amount) as total
            FROM expenses
            WHERE date BETWEEN ? AND ?
            GROUP BY category
        """, (
            summary_request.start_date,
            summary_request.end_date
        ))

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


@app.get("/categories")
def get_categories():
    with open(CATEGORIES_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


# =========================

# RUN SERVER

# =========================

# Run using:

# uvicorn server:app --reload
