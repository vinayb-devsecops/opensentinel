import sqlite3

DB_FILE = "database/opensentinel.db"

def get_connection():
    return sqlite3.connect(DB_FILE)

def initialize():

    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS cves (
            cve_id TEXT PRIMARY KEY,
            source TEXT,
            published TEXT,
            status TEXT,
            cvss_score REAL
        )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize()
    print("Database initialized")
