import pandas as pd

from src.constants.game_titles import GameTitle
from src.constants.columns import SteamChartsColumns


def get_oldest_month(game_title: GameTitle) -> str:
    df = pd.read_csv(game_title.csv_path)
    return df.iloc[-1][SteamChartsColumns.MONTH]