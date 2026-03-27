from flask import Flask, render_template, request
from datetime import datetime
import sqlite3

app = Flask(__name__)

DB_NAME = 'monitor.db'

SUMMARY_QUERY = """
    SELECT status, COUNT(*)
    FROM edi_transactions
    GROUP BY status
    ORDER BY status;
"""

DETAILS_QUERY = """
    SELECT id, edi_ref, customer, doc_type, status, created_at, updated_at, error_message
    FROM edi_transactions
    ORDER BY updated_at DESC, created_at DESC, id DESC
    LIMIT 50;
"""

@app.route('/')
def dashboard():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(SUMMARY_QUERY)
    rows = cursor.fetchall()

    summary_dict = {status: count for status, count in rows}

    status_summary = [
    ("Failed", summary_dict.get("Failed", 0)),
    ("Pending", summary_dict.get("Pending", 0)),
    ("Processed", summary_dict.get("Processed", 0)),
    ]

    cursor.execute("""
    SELECT MAX(updated_at)
    FROM edi_transactions
    """)
    last_updated = cursor.fetchone()[0]

    cursor.execute(DETAILS_QUERY)
    details_rows = cursor.fetchall()

    conn.close()

    return render_template(
        'dashboard.html',
        status_summary=status_summary,
        details_rows=details_rows,
        last_updated=last_updated,
    )

if __name__ == '__main__':
    app.run(debug=True)
    
