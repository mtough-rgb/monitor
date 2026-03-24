import sqlite3

DB_NAME = "monitor.db"

sample_data = [
    ("EDI1002", "Customer B", "Invoice", "Processed", "2026-03-24 08:30:00", "2026-03-24 08:45:00", ""),
    ("EDI1003", "Customer C", "ASN", "Failed", "2026-03-24 09:00:00", "2026-03-24 09:05:00", "Missing customer code"),
    ("EDI1004", "Customer A", "Order", "Processed", "2026-03-24 09:10:00", "2026-03-24 09:20:00", ""),
    ("EDI1005", "Customer D", "Invoice", "Pending", "2026-03-24 09:25:00", "2026-03-24 09:25:00", ""),
]

def seed_data():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type = 'table' AND name = 'edi_transactions'
        """
    )
    if cursor.fetchone() is None:
        conn.close()
        raise RuntimeError(
            "Table 'edi_transactions' does not exist. Run init_db.py first."
        )

    existing_refs = {
        row[0] for row in cursor.execute("SELECT edi_ref FROM edi_transactions")
    }
    rows_to_insert = [row for row in sample_data if row[0] not in existing_refs]

    if rows_to_insert:
        cursor.executemany(
            """
            INSERT INTO edi_transactions (
                edi_ref,
                customer,
                doc_type,
                status,
                created_at,
                updated_at,
                error_message
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            rows_to_insert,
        )
        conn.commit()

    conn.close()
    print(
        f"Inserted {len(rows_to_insert)} rows into '{DB_NAME}'. "
        f"Skipped {len(sample_data) - len(rows_to_insert)} existing rows."
    )


def main():
    seed_data()


if __name__ == "__main__":
    main()
