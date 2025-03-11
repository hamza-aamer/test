from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route("/")
def hello():
    db_host = os.environ.get("POSTGRES_HOST", "localhost")
    db_user = os.environ.get("POSTGRES_USER", "myuser")
    db_password = os.environ.get("POSTGRES_PASSWORD", "mypassword")
    db_name = os.environ.get("POSTGRES_DB", "mydb")
    try:
        conn = psycopg2.connect(host=db_host, user=db_user, password=db_password, dbname=db_name)
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        cur.close()
        conn.close()
        return f"Connected to PostgreSQL version: {version}"
    except Exception as e:
        return f"Database connection failed: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
