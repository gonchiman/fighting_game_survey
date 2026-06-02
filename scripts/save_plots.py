import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from src.constants.columns import SteamChartsColumns
from src.constants.game_titles import GameTitle
from src.graphs.graphs import Graphs


for game_title in GameTitle:
    Graphs.plot(game_title, SteamChartsColumns.PEAK_PLAYERS, save=True)
    Graphs.plot(game_title, SteamChartsColumns.AVG_PLAYERS, save=True)
    Graphs.cumulative_plot(game_title, SteamChartsColumns.PEAK_PLAYERS, save=True)
    Graphs.cumulative_plot(game_title, SteamChartsColumns.AVG_PLAYERS, save=True)
    Graphs.cumulative_play_hours_plot(game_title, save=True)