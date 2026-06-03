import re
from urllib.parse import urljoin

from pathlib import Path
import pandas as pd
import requests
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parent.parent
FGCHARTS_URL = "https://fgcharts.info/"
APP_ID_PATTERN = re.compile(r"/app/(\d+)")


def extract_app_id(url: str) -> int | None:
    match = APP_ID_PATTERN.search(url)
    if match is None:
        return None
    return int(match.group(1))


def get_fighting_game_ids() -> pd.DataFrame:
    response = requests.get(FGCHARTS_URL, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    rows = []

    for tr in soup.select("tr"):
        tds = tr.select("td")

        if not tds:
            continue

        title = tds[0].get_text(strip=True)

        store_url = None
        steamcharts_url = None
        app_id = None

        for a in tr.select("a[href]"):
            href = urljoin(FGCHARTS_URL, a["href"])

            if "store.steampowered.com/app/" in href:
                store_url = href
                app_id = extract_app_id(href)

            elif "steamcharts.com/app/" in href:
                steamcharts_url = href
                if app_id is None:
                    app_id = extract_app_id(href)

        if app_id is not None:
            rows.append(
                {
                    "title": title,
                    "app_id": app_id,
                    "steamcharts_url": steamcharts_url,
                    "store_url": store_url,
                }
            )

    return pd.DataFrame(rows)


df = get_fighting_game_ids()
df.to_csv(BASE_DIR / "data/utils/fighting_game_ids.csv", index=False, encoding="utf-8-sig")

print(df.head())