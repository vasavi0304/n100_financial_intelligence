import sqlite3
from pathlib import Path

DB_PATH = Path("db/nifty100.db")
SCHEMA_PATH = Path("db/schema.sql")


def create_database():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DB_PATH)

    with open(SCHEMA_PATH, "r", encoding="utf-8") as file:
        schema_sql = file.read()

    connection.executescript(schema_sql)
    connection.commit()
    connection.close()

    print(f"Database created successfully at {DB_PATH}")


if __name__ == "__main__":
    create_database()