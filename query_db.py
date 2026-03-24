import sqlite3

DB_NAME = "monitor.db"

def main():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM edi_transactions")
    rows = cursor.fetchall()

    print(f"Found {len(rows)} rows in edi_transactions table:")
    for row in rows:
        print(row)

    conn.close()

if __name__ == "__main__":
    main()