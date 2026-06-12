import sqlite3

DB_FILE = "database/opensentinel.db"

def get_summary():

    conn = sqlite3.connect(DB_FILE)

    total = conn.execute(
        "select count(*) from cves"
    ).fetchone()[0]

    status_counts = conn.execute("""
        select status, count(*)
        from cves
        group by status
    """).fetchall()

    conn.close()

    return {
        "total_cves": total,
        "status_counts": status_counts
    }
