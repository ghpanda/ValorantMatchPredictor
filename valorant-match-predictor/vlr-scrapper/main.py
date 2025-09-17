from scraper.teams import getAllTeams
from storage.awsrds import insert_teams, insert_players, insert_staff
from scraper.players import scrape_players


if __name__ == "__main__":
    # Scrape all VCT Teams 
    data = getAllTeams()
    # Insert into AWS RDS
    insert_teams(data)
    for region in data:
        region_name = region["region"]
        for team in region["teams"]:
            # Scrape Players for each team
            players, staff = scrape_players(team["team_url"])
            insert_players(team_name=team["team_name"], players_data=players)
            # insert_staff(team_name=team["team_name"], staff_data=staff)
            
    # Insert into AWS RDS