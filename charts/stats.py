import sqlite3

DB_FILE = "database/opensentinel.db"

def get_summary():

    conn = sqlite3.connect(DB_FILE)

    total = conn.execute(
        "select count(*) from cves"
    ).fetchone()[0]

    conn.close()

    return {
        "total_cves": total
    }

if __name__ == "__main__":
    print(get_summary())
