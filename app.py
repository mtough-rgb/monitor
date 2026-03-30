from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

DB_NAME = 'monitor.db'

SUMMARY_QUERY = """
    SELECT COUNT(*)
    FROM failed_edi_files;
"""

DETAILS_QUERY = """
    SELECT id, file_name, trading_partner_id, purchase_order_number, loaded_at
    FROM failed_edi_files
    ORDER BY loaded_at DESC, id DESC
    LIMIT 50;
"""

@app.route('/')
def dashboard():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(SUMMARY_QUERY)
    total_failed_files = cursor.fetchone()[0]

    cursor.execute("""
    SELECT MAX(loaded_at)
    FROM failed_edi_files
    """)
    last_updated = cursor.fetchone()[0]

    cursor.execute(DETAILS_QUERY)
    details_rows = cursor.fetchall()

    conn.close()

    return render_template(
        'dashboard.html',
        total_failed_files=total_failed_files,
        details_rows=details_rows,
        last_updated=last_updated,
    )

if __name__ == '__main__':
    app.run(debug=True)
    
