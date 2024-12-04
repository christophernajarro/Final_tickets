import time
import os
import psycopg2
from psycopg2 import OperationalError

def wait_for_db():
    while True:
        try:
            conn = psycopg2.connect(
                dbname=os.getenv("POSTGRES_DB"),
                user=os.getenv("POSTGRES_USER"),
                password=os.getenv("POSTGRES_PASSWORD"),
                host=os.getenv("DB_HOST", "db"),
                port=os.getenv("DB_PORT", 5432),
            )
            conn.close()
            print("Database is ready!")
            break
        except OperationalError:
            print("Database is not ready yet. Waiting for 5 seconds...")
            time.sleep(5)

if __name__ == "__main__":
    wait_for_db()