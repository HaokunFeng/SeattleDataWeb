import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()


db_user = os.getenv('DB_USER')
db_pw = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

# Ensure all required environment variables are defined
if None in (db_user, db_pw, db_host, db_name):
    raise ValueError("One or more required environment variables are not defined.")

# Set a default port if DB_PORT is not provided
default_db_port = 5432  # Change this to your default PostgreSQL port
db_port = int(db_port) if db_port and db_port.isdigit() else default_db_port

conn_str = f'postgresql://{db_user}:{db_pw}@{db_host}:{db_port}/{db_name}'


def get_db_conn():
    conn = psycopg2.connect(conn_str)
    conn.autocommit = True
    return conn
