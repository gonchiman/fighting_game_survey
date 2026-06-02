from matplotlib import pyplot as plt
import pandas as pd

from src.constants.game_titles import GameTitle
from src.entities.period import Period
from src.constants.columns import SteamChartsColumns


class Graphs:
    @staticmethod
    def show_plot(game_title: GameTitle, column: str, period: Period = None) -> None:
        df = pd.read_csv(game_title.csv_path)

        # "Last 30 Days" は月データではないので除外
        df = df[df[SteamChartsColumns.MONTH] != "Last 30 Days"]

        # 古い月 → 新しい月 の順にする
        df = df.iloc[::-1].reset_index(drop=True)

        if period is not None:
            start_index = df.index[df[SteamChartsColumns.MONTH] == period.start][0]
            end_index = df.index[df[SteamChartsColumns.MONTH] == period.end][0]

            if start_index > end_index:
                start_index, end_index = end_index, start_index

            df = df.iloc[start_index:end_index + 1].reset_index(drop=True)

        months = df[SteamChartsColumns.MONTH]
        values = df[column]

        x = range(len(df))

        plt.figure(figsize=(12, 6))
        plt.plot(x, values, marker="o")

        plt.xticks(
            ticks=x,
            labels=months,
            rotation=90
        )

        plt.xlabel("Month")
        plt.ylabel(column)
        plt.title(f"{game_title} - {column}")
        plt.tight_layout()
        plt.show()

    @staticmethod
    def show_cumulative_plot(game_title: GameTitle, column: str, period: Period = None) -> None:
        df = pd.read_csv(game_title.csv_path)

        # "Last 30 Days" は月データではないので除外
        df = df[df[SteamChartsColumns.MONTH] != "Last 30 Days"]

        # 古い月 → 新しい月 の順にする
        df = df.iloc[::-1].reset_index(drop=True)

        if period is not None:
            start_index = df.index[df[SteamChartsColumns.MONTH] == period.start][0]
            end_index = df.index[df[SteamChartsColumns.MONTH] == period.end][0]

            if start_index > end_index:
                start_index, end_index = end_index, start_index

            df = df.iloc[start_index:end_index + 1].reset_index(drop=True)

        months = df[SteamChartsColumns.MONTH]
        values = df[column].cumsum()

        x = range(len(df))

        plt.figure(figsize=(12, 6))
        plt.plot(x, values, marker="o")

        plt.xticks(
            ticks=x,
            labels=months,
            rotation=90
        )

        plt.xlabel("Month")
        plt.ylabel(f"Cumulative {column}")
        plt.title(f"{game_title} - Cumulative {column}")
        plt.tight_layout()
        plt.show()