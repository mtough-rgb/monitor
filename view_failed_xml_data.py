import sqlite3

DB_NAME = "monitor.db"

query = """
SELECT
    id,
    file_name,
    trading_partner_id,
    purchase_order_number,
    loaded_at
FROM failed_edi_files
ORDER BY id DESC;
"""

def main():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(query)
    rows = cursor.fetchall()

    conn.close()

    if not rows:
        print("No rows found.")
        return

    for row in rows:
        print(row)

if __name__ == "__main__":
    main()