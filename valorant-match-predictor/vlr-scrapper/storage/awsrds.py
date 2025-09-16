import psycopg2
from dotenv import load_dotenv
import os 

load_dotenv()

def getConnection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

def insert_teams(regions_data):
    conn = getConnection()
    cur = conn.cursor()

    for region in regions_data:
        for team in region["teams"]:
            cur.execute(""" 
                INSERT INTO TEAMS (team_name, country, points, team_url, region)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (team_name) DO NOTHING;
                """, (
                    team["team_name"],
                    team["country"],
                    team["points"],
                    team["team_url"],
                    team["region"],
                    ))
    conn.commit()
    cur.close()
    conn.close()
    print("Data inserted successfully.")

def fetch_teams():
    conn = getConnection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM TEAMS;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
    return rows 


