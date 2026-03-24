import sqlite3

db_name = 'monitor.db'

query = "SELECT * FROM edi_transactions"

def main():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    conn.close()

    if not rows:
        print("No data found in the database.")
        return
    
    for row in rows:
        print(row)

if __name__ == "__main__":
    main()

    