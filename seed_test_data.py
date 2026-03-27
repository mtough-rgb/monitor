import sqlite3

DB_NAME = "monitor.db"

sample_data = [
    ("EDI1002", "Customer B", "Invoice", "Processed", "2026-03-24 08:30:00", "2026-03-24 08:45:00", ""),
    ("EDI1003", "Customer C", "ASN", "Failed", "2026-03-24 09:00:00", "2026-03-24 09:05:00", "Missing customer code"),
    ("EDI1004", "Customer A", "Order", "Processed", "2026-03-24 09:10:00", "2026-03-24 09:20:00", ""),
    ("EDI1005", "Customer D", "Invoice", "Pending", "2026-03-24 09:25:00", "2026-03-24 09:25:00", ""),
]

insert_sql = """
INSERT INTO edi_transactions (
    edi_ref,
    customer,
    doc_type,
    status,
    created_at,
    updated_at,
    error_message
)
VALUES (?, ?, ?, ?, ?, ?, ?)
"""

def main():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.executemany(insert_sql, sample_data)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()