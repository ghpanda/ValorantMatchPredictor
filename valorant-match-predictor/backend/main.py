from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

@app.get("/teams")
def get_teams():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM TEAMS;")
    teams = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": t[0], "name": t[1], "link": t[5]} for t in teams]