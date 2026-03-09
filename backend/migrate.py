import sqlite3
import os

def migrate():
    db_path = "pc_builder.db"
    if not os.path.exists(db_path):
        print(f"Database not found at {db_path}")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        cursor.execute("ALTER TABLE components ADD COLUMN image_url TEXT")
        conn.commit()
        print("Successfully added image_url column.")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e).lower():
            print("Column image_url already exists.")
        else:
            print(f"Error during migration: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    migrate()
