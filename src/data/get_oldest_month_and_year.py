import pandas as pd

from src.constants.game_titles import GameTitle
from src.constants.columns import SteamChartsColumns


def get_oldest_month_and_year(game_title: GameTitle) -> tuple[str, str]:
    df = pd.read_csv(game_title.csv_path)
    oldest_month_year = df.iloc[-1][SteamChartsColumns.MONTH].split()
    return oldest_month_year[0], oldest_month_year[1]