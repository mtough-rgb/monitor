import sqlite3

DB_NAME = 'monitor.db'

create_table_sql = """
CREATE TABLE IF NOT EXISTS edi_transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    edi_ref TEXT NOT NULL,
    customer TEXT,
    doc_type TEXT,
    status TEXT NOT NULL,
    created_at TEXT,
    updated_at TEXT,
    error_message TEXT
);
"""

def main():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(create_table_sql)
    conn.commit()
    conn.close()
    print(f"Database '{DB_NAME}' initialized with 'edi_transactions' table.")

if __name__ == "__main__":
    main()
