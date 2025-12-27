import sqlite3
from werkzeug.security import generate_password_hash
import os
import sys

# Add parent directory to path to allow imports when run as script
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.models import DB_NAME

conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()

# Drop old table if exists (for fresh start)
cur.execute("DROP TABLE IF EXISTS users")

# Create users table with email
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

# Insert admin user (example)
cur.execute(
    "INSERT OR IGNORE INTO users (username, email, password) VALUES (?, ?, ?)",
    ("admin", "admin@example.com", generate_password_hash("admin123"))
)

conn.commit()
conn.close()

print("Database created successfully. Admin user added.")
