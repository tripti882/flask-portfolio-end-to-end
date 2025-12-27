import sqlite3
import os
from flask_login import UserMixin

# Get the root directory (parent of app/)
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_NAME = os.path.join(root_dir, "users.db")


# ------------------------
# User Model
# ------------------------
class User(UserMixin):
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<User {self.username}>"


# ------------------------
# Helper functions
# ------------------------
def get_db_connection():
    """Get a database connection."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Access columns by name
    return conn


def get_user_by_username(username):
    """Get a user by username."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return User(id=row["id"], username=row["username"], email=row["email"], password=row["password"])
    return None


def get_user_by_email(email):
    """Get a user by email."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return User(id=row["id"], username=row["username"], email=row["email"], password=row["password"])
    return None


def get_user_by_id(user_id):
    """Get a user by ID (required by Flask-Login)."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return User(id=row["id"], username=row["username"], email=row["email"], password=row["password"])
    return None


def create_user(username, email, hashed_password):
    """Create a new user in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            (username, email, hashed_password)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        raise ValueError("Username or email already exists")
    finally:
        conn.close()
