import sqlite3

def init_db():
    conn = sqlite3.connect("stats.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS stats (
        date TEXT PRIMARY KEY,
        followers INTEGER,
        likes INTEGER,
        videos INTEGER
    )""")
    conn.commit()
    conn.close()

def save_stats(date, followers, likes, videos):
    conn = sqlite3.connect("stats.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO stats VALUES (?, ?, ?, ?)", (date, followers, likes, videos))
    conn.commit()
    conn.close()