import sqlite3

DB_NAME = "monitor.db"

create_table_sql = """CREATE TABLE IF NOT EXISTS failed_edi_files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_name TEXT NOT NULL UNIQUE,
    trading_partner_id TEXT,
    purchase_order_number TEXT,
    loaded_at TEXT DEFAULT CURRENT_TIMESTAMP
);"""

def main():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(create_table_sql)

    conn.commit()
    conn.close()

    print("failed_edi_files table created successfully.")

if __name__ == "__main__":
    main()