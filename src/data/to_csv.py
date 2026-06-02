from io import StringIO
from urllib.parse import urljoin

import pandas as pd
from playwright.sync_api import sync_playwright

from src.constants.game_titles import GameTitle
from src.constants.urls import BASE_URL


class ToCSV:
    @classmethod
    def to_csv(cls, game_title: GameTitle) -> None:
        df = cls._get_df(game_title)
        df.to_csv(game_title.csv_path, index=False, encoding="utf-8-sig")

    @staticmethod
    def _get_df(game_title: GameTitle) -> pd.DataFrame:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)

            try:
                page = browser.new_page()

                page.goto(urljoin(BASE_URL, str(game_title.app_id)), 
                        wait_until="domcontentloaded", 
                        timeout=30000
                )

                html = page.content()

                tables = pd.read_html(StringIO(html))

                return tables[0]

            finally:
                browser.close()