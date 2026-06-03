from matplotlib import pyplot as plt
import pandas as pd

from src.entities.period import Period
from src.constants.columns import SteamChartsColumns, TotalAnalysisColumns
from src.constants.paths import PLOT_IMAGES_GAMES_DIR, PLOT_IMAGES_TOTAL_ANALYSIS_DIR
from src.constants.game_titles import GameTitle
from src.data.aggregate import create_total_analysis_df


class Graphs:
    @staticmethod
    def plot(game_title: GameTitle, column: str, period: Period = None, save: bool = False) -> None:
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
        plt.title(f"{game_title.title} - {column}")
        plt.tight_layout()
        if save:
            plt.savefig(PLOT_IMAGES_GAMES_DIR / f"{game_title.name.lower()}_{column}_plot.png")
            plt.close()
        else:
            plt.show()

    @staticmethod
    def cumulative_plot(game_title: GameTitle, column: str, period: Period = None, save: bool = False) -> None:
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
        plt.title(f"{game_title.title} - Cumulative {column}")
        plt.tight_layout()
        if save:
            plt.savefig(PLOT_IMAGES_GAMES_DIR / f"{game_title.name.lower()}_{column}_cumulative_plot.png")
            plt.close()
        else:
            plt.show()

    @staticmethod
    def cumulative_play_hours_plot(game_title: GameTitle, period: Period = None, save: bool = False) -> None:
        df = pd.read_csv(game_title.csv_path)

        # "Last 30 Days" は月データではないので除外
        df = df[df[SteamChartsColumns.MONTH] != "Last 30 Days"]
        df["Estimated Play Hours (Millions)"] = df[SteamChartsColumns.AVG_PLAYERS] * 720 / 1_000_000

        # 古い月 → 新しい月 の順にする
        df = df.iloc[::-1].reset_index(drop=True)

        if period is not None:
            start_index = df.index[df[SteamChartsColumns.MONTH] == period.start][0]
            end_index = df.index[df[SteamChartsColumns.MONTH] == period.end][0]

            if start_index > end_index:
                start_index, end_index = end_index, start_index

            df = df.iloc[start_index:end_index + 1].reset_index(drop=True)

        months = df[SteamChartsColumns.MONTH]
        values = df["Estimated Play Hours (Millions)"].cumsum()

        x = range(len(df))

        plt.figure(figsize=(12, 6))
        plt.plot(x, values, marker="o")

        plt.xticks(
            ticks=x,
            labels=months,
            rotation=90
        )

        plt.xlabel("Month")
        plt.ylabel("Cumulative Estimated Play Hours (Millions)")
        plt.title(f"{game_title.title} - Cumulative Estimated Play Hours (Millions)")
        plt.tight_layout()
        if save:
            plt.savefig(PLOT_IMAGES_GAMES_DIR / f"{game_title.name.lower()}_estimated_play_hours_cumulative_plot.png")
            plt.close()
        else:
            plt.show()

    @staticmethod
    def total_cumulative_play_hours_plot(period: Period = None, save: bool = False) -> None:
        df = create_total_analysis_df()

        df["Estimated Play Hours (Millions)"] = df[TotalAnalysisColumns.CUMULATIVE_ESTIMATED_PLAY_HOURS] / 1_000_000

        if period is not None:
            start_index = df.index[df[TotalAnalysisColumns.MONTH] == period.start][0]
            end_index = df.index[df[TotalAnalysisColumns.MONTH] == period.end][0]

            if start_index > end_index:
                start_index, end_index = end_index, start_index

            df = df.iloc[start_index:end_index + 1].reset_index(drop=True)

        months = df[TotalAnalysisColumns.MONTH]
        values = df["Estimated Play Hours (Millions)"]

        x = range(len(df))

        plt.figure(figsize=(19, 9))
        plt.plot(x, values)

        plt.xticks(
            ticks=x,
            labels=months,
            rotation=90
        )

        plt.xlabel("Month")
        plt.ylabel("Cumulative Estimated Play Hours (Millions)")
        plt.title("Monthly Total Cumulative Play Hours of Major Fighting Games on Steam")
        plt.tight_layout()

        plt.grid(True)
        plt.tight_layout()

        if save:
            plt.savefig(PLOT_IMAGES_TOTAL_ANALYSIS_DIR / f"total_estimated_play_hours_cumulative_plot.png")
            plt.close()
        else:
            plt.show()