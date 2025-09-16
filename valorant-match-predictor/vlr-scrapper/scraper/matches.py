from scraper.utils import fetch_html, parse_html
from pprint import pprint

def scrape_matches(limit=10):
    url = "https://www.vlr.gg/matches/results"
    html = fetch_html(url)
    soup = parse_html(html)

    matches = []
    for match in soup.select(".wf-module-item")[:limit]:
        teams = match.select(".match-item-vs-team") 
        if len(teams) < 2:
            continue
        team1_name = teams[0].select_one(".match-item-vs-team-name").get_text(strip=True)
        team1_score = teams[0].select_one(".match-item-vs-team-score").get_text(strip=True)
        team2_name = teams[1].select_one(".match-item-vs-team-name").get_text(strip=True)
        team2_score = teams[1].select_one(".match-item-vs-team-score").get_text(strip=True)
        
        matches.append({
            "team1": {"name": team1_name, "score": team1_score, "Winner": team1_score > team2_score},
            "team2": {"name": team2_name, "score": team2_score, "Winner": team2_score > team1_score},
        })
    return matches


if __name__ == "__main__":
    data = scrape_matches(limit=1)
    pprint(data)