import google.generativeai as genai
from serpapi import GoogleSearch
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")


def search_team_defense(team):
    q = f"{team} NBA defensive scheme rotations coverages help principles scouting"
    search = GoogleSearch({"q": q, "api_key": os.getenv("SERPAPI_KEY"), "num": 8})
    res = search.get_dict()

    out = []
    if "organic_results" in res:
        for r in res["organic_results"]:
            if "snippet" in r:
                out.append(r["snippet"])

    return "\n".join(out[:6])


def format_offensive_profile(data):
    return "\n".join(f"{ptype}: {pts} PTS" for ptype, pts in data)


def format_defensive_profile(data):
    return "\n".join(f"{ptype}: {ppp} PPP (Rank {rank})" for ptype, ppp, rank in data)


def analyze_matchup(player_name, offensive_profile, defensive_profile, team_name):

    supplemental_text = search_team_defense(team_name)

    prompt = f"""
    You are an NBA scouting report generator.

    Player: {player_name}
    Opponent: {team_name}

    Offensive Play-Type Profile:
    {format_offensive_profile(offensive_profile)}

    Defensive PPP Profile:
    {format_defensive_profile(defensive_profile)}

    Additional Scouting Info:
    {supplemental_text}

    Write a professional NBA coaching scouting report on how {player_name} is expected to perform.
    """

    return model.generate_content(prompt).text
