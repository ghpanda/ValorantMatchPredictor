from scraper.utils import fetch_html, parse_html
from pprint import pprint
from scraper.matches import scrape_matches
import os 
import json 

def getAllTeams():
    url = "https://www.vlr.gg/vct-2025/standings"
    html = fetch_html(url)
    soup = parse_html(html)
    regions = []
    i = 1
    # Get all Regions
    for region in soup.select("div.eg-standing-group"):
        # Get Region Name
        region_name = region.select_one(".wf-label").get_text(strip=True)
        # print(region_name)
        teams = []
        # Loop over the the regions table rows 
        for team in region.select("tr"):
            team_cell = team.select_one("td.eg-standing-group-team")
            # print(team_cell)
            if not team_cell:
                continue
            # Get Link 
            link = team_cell.select_one("a")["href"]
            link = "https://www.vlr.gg" + link
            # print("LINK:", link)
            # Get Team Name
            team_name = team_cell.select_one("div[style*='font-weight: 700']").get_text(strip=True)
            # print("TEAM NAME:", team_name)
            # Get Country
            country = team_cell.select_one(".ge-text-light").get_text(strip=True)
            # print("COUNTRY:", country)
            # Get Points
            points = team.select("td")[1].get_text(strip=True)
            # print("POINTS:", points)
            
            teams.append({
                "team_name": team_name,
                "country": country,
                "points": points,
                "link": link,
                "region": region_name,
            })
        regions.append({
            "Region": region_name,
            "Teams": teams,
        })

    # Save to JSON file
    os.makedirs("data/teams.json", exist_ok=True)
    with open("data/teams.json", "w", encoding="utf-8") as f:
        json.dump(regions, f, indent=4)

    return regions


if __name__ == "__main__":
    data = getAllTeams()
    pprint(data)