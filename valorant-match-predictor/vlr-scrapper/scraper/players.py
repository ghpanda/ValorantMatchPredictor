from scraper.utils import fetch_html, parse_html   
from pprint import pprint

def scrape_players(team_url):
    html = fetch_html(team_url)
    soup = parse_html(html)

    players = []
    staff = []

    for item in soup.select("div.team-roster-item"):
        profile_url = "https://www.vlr.gg" + item.select_one("a")["href"]
        # print("PROFILE URL:", profile_url)

        ign = item.select_one(".team-roster-item-name-alias").get_text(strip=True)
        # print("IGN:", ign)  
        name = item.select_one(".team-roster-item-name-real")
        if name:
            name = name.get_text(strip=True)
        else:
            name = ign  # Fallback to IGN if full name is missing
        # print("NAME:", name)
        
        role = item.select_one(".wf-tag")
        if role:
            role = role.get_text(strip=True).title()
        else:
            role = "Player"
        # print("ROLE:", role)

        player = {
            "ign": ign,
            "name": name,
            "role": role,
            "profile_url": profile_url,
        }

        if role.lower() in ["player", "sub", "inactive"]:
            players.append(player)
        else:
            staff.append(player)
        
    return players, staff

if __name__ == "__main__":
    team_url = "https://www.vlr.gg/team/2355/kr-esports"
    players, staff = scrape_players(team_url)
    # print("Players:", players)
    # print("Staff:", staff)


