import calendar
from functools import reduce

import pandas as pd

from src.constants.columns import SteamChartsColumns
from src.constants.game_titles import GameTitle


def load_game_avg_players_df(game_title: GameTitle) -> pd.DataFrame:
    df = pd.read_csv(game_title.csv_path)

    df = df[df[SteamChartsColumns.MONTH] != "Last 30 Days"].copy()

    df["Date"] = pd.to_datetime(
        df[SteamChartsColumns.MONTH],
        format="%B %Y"
    )

    df = df[["Date", SteamChartsColumns.AVG_PLAYERS]].copy()

    df = df.rename(
        columns={
            SteamChartsColumns.AVG_PLAYERS: game_title.title
        }
    )

    return df


def create_total_analysis_df() -> pd.DataFrame:
    game_dfs = [
        load_game_avg_players_df(game_title)
        for game_title in GameTitle
    ]

    df = reduce(
        lambda left, right: pd.merge(
            left,
            right,
            on="Date",
            how="outer"
        ),
        game_dfs
    )

    df = df.sort_values("Date").reset_index(drop=True)

    game_columns = [
        game_title.title
        for game_title in GameTitle
    ]

    # 未発売期間は 0 として扱う
    df[game_columns] = df[game_columns].fillna(0)

    # 格闘ゲーム全体の平均プレイヤー数
    df["Total Avg. Players"] = df[game_columns].sum(axis=1)

    # 月の時間数
    df["Hours in Month"] = df["Date"].apply(
        lambda date: calendar.monthrange(date.year, date.month)[1] * 24
    )

    # 月間推定プレイ時間
    df["Estimated Play Hours"] = (
        df["Total Avg. Players"] * df["Hours in Month"]
    )

    # 累積推定プレイ時間
    df["Cumulative Estimated Play Hours"] = (
        df["Estimated Play Hours"].cumsum()
    )

    # 表示用の月
    df[SteamChartsColumns.MONTH] = df["Date"].dt.strftime("%B %Y")

    return df