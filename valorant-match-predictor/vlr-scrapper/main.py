from scraper.teams import getAllTeams
from storage.awsrds import insert_teams, fetch_teams

if __name__ == "__main__":
    # Scrape Data 
    data = getAllTeams()
    # Insert into AWS RDS
    insert_teams(data)
    # Fetch from AWS RDS
    # teams = fetch_teams()
    # for team in teams:
    #     print(team) 