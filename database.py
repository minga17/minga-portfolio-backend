import sqlite3
import os

DATABASE = os.environ.get('DATABASE_PATH', 'portfolio.db')

def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    db = get_db()
    db.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            number      INTEGER NOT NULL,
            title       TEXT    NOT NULL,
            category    TEXT,
            status      TEXT    DEFAULT 'planned',
            type        TEXT    DEFAULT 'data',
            date        TEXT,
            date_sub    TEXT,
            problem     TEXT,
            what_i_did  TEXT,
            insights    TEXT,
            tags        TEXT,
            github_url  TEXT,
            kaggle_url  TEXT,
            live_url    TEXT,
            powerbi_url TEXT,
            chart_image TEXT
        )
    ''')
    db.execute('''
        CREATE TABLE IF NOT EXISTS pageviews (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            page      TEXT,
            ip_hash   TEXT,
            timestamp TEXT
        )
    ''')
    db.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            name      TEXT,
            email     TEXT,
            message   TEXT,
            timestamp TEXT
        )
    ''')
    db.commit()
    db.close()
