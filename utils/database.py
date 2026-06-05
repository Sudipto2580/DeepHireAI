import sqlite3

DB = "database/candidates.db"

def create_database():

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS candidates(

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    
    filename TEXT,

    score REAL,

    semantic REAL,

    skill REAL,

    matched TEXT,

    missing TEXT

    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    fullname TEXT,

    username TEXT UNIQUE,

    email TEXT UNIQUE,

    password TEXT,

    phone TEXT,

    linkedin TEXT,

    github TEXT,

    portfolio TEXT,

    twitter TEXT,

    instagram TEXT,

    theme TEXT DEFAULT 'Dark',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)


    conn.commit()
    conn.close()

from utils.supabase_db import supabase

def insert_candidate(candidate):

    supabase.table(
        "candidates"
    ).insert({

        "filename":
        candidate["name"],

        "score":
        candidate["score"],

        "semantic":
        candidate["semantic"],

        "skill":
        candidate["skill"],

        "matched":
        candidate["matched"],

        "missing":
        candidate["missing"]

    }).execute()

def get_all_candidates():

    response = supabase.table(
        "candidates"
    ).select(
        "*"
    ).order(
        "score",
        desc=True
    ).execute()

    return response.data
 