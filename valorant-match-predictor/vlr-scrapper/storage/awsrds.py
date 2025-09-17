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
                ON CONFLICT (team_name) 
                DO UPDATE SET
                    country = EXCLUDED.country,
                    points = EXCLUDED.points,
                    team_url = EXCLUDED.team_url,
                    region = EXCLUDED.region;
                """, 
                (
                    team["team_name"],
                    team["country"],
                    team["points"],
                    team["team_url"],
                    team["region"],
                ))        
            print(f"{team['team_name']} inserted successfully.")
    conn.commit()
    cur.close()
    conn.close()

def insert_players(team_name, players_data):
    conn = getConnection()
    cur = conn.cursor()

    for player in players_data:
        # print(player)
        cur.execute("SELECT team_id FROM TEAMS WHERE team_name = %s;", (team_name,))
        team_id = cur.fetchone()[0]  # Extract the actual ID from the tuple
        # print("TEAM ID:", team_id)
        cur.execute(""" 
            INSERT INTO PLAYERS (team_id, ign, full_name, role_, profile_url)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (ign) 
            DO UPDATE SET
                team_id = EXCLUDED.team_id,
                full_name = EXCLUDED.full_name,
                role_ = EXCLUDED.role_,
                profile_url = EXCLUDED.profile_url;
            """, (
                team_id,
                player["ign"],
                player["name"],
                player["role"],
                player["profile_url"],
                ))
        print(f"Players for {team_name} have been inserted successfully.")
    conn.commit()
    cur.close()
    conn.close()
    

def insert_staff(team_name, staff_data):
    conn = getConnection()
    cur = conn.cursor()

    for staff_member in staff_data:
        cur.execute("""
            INSERT INTO PLAYERS (team_id, ign, name, role, profile_url)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (ign) DO NOTHING;
            """, (
                team_id,
                staff_member["ign"],
                staff_member["name"],
                staff_member["role"],
                staff_member["profile_url"],
                ))
    conn.commit()
    cur.close()
    conn.close()
    print("Staff data inserted successfully.")
