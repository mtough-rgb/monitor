import sqlite3

db_name = 'monitor.db'

query = """
SELECT status, COUNT(*)
FROM edi_transactions
GROUP BY status
ORDER BY status;
"""

def main():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    conn.close()

    if not rows:
        print("No data found in the database.")
        return
    
    print("Status Summary:")    
    print("-----------------")
   
    for status, count in rows:
        print(f"{status}: {count}")


if __name__ == "__main__":
    main()