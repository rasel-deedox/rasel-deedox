import os
import re
import json
import datetime
import requests
from bs4 import BeautifulSoup

GITHUB_USERNAME = os.getenv("GH_USERNAME", "rasel-deedox")

def fetch_contributions():
    url = f"https://github.com/users/{GITHUB_USERNAME}/contributions"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers, timeout=20)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")
    days = []

    # Build tooltip lookup if present
    tooltips = {}
    for tip in soup.find_all("tool-tip"):
        for_id = tip.get("for")
        if for_id:
            tooltips[for_id] = " ".join(tip.text.split())

    for td in soup.find_all("td", class_="ContributionCalendar-day"):
        date = td.get("data-date")
        level_str = td.get("data-level", "0")
        cell_id = td.get("id", "")
        if not date:
            continue
        level = int(level_str) if str(level_str).isdigit() else 0
        tip_text = tooltips.get(cell_id, "")
        count = 0
        m = re.search(r"(\d+)\s+contribution", tip_text)
        if m:
            count = int(m.group(1))
        days.append({
            "date": date,
            "level": level,
            "count": count
        })

    days.sort(key=lambda x: x["date"])

    # Compute streaks
    longest_streak = 0
    current_streak = 0
    temp_streak = 0
    for d in days:
        if d["level"] > 0:
            temp_streak += 1
            if temp_streak > longest_streak:
                longest_streak = temp_streak
        else:
            temp_streak = 0

    # Current streak from latest day backwards
    for d in reversed(days):
        if d["level"] > 0:
            current_streak += 1
        else:
            # Allow today to be 0 if yesterday was active
            if d == days[-1]:
                continue
            break

    h2 = soup.find("h2", id="js-contribution-activity-description")
    total_text = "Contributions in the last year"
    if h2:
        total_text = " ".join(h2.text.split())

    os.makedirs("data", exist_ok=True)
    payload = {
        "username": GITHUB_USERNAME,
        "updated_at": datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
        "total_text": total_text,
        "longest_streak": longest_streak,
        "current_streak": current_streak,
        "days": days
    }
    with open("data/contributions.json", "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    print(f"Saved {len(days)} days of contributions for {GITHUB_USERNAME}")

if __name__ == "__main__":
    fetch_contributions()

