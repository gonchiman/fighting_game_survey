import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(BASE_DIR))

from src.graphs.graphs import Graphs
from src.entities.period import Period
from src.constants.game_titles import GameTitle
from src.constants.columns import SteamChartsColumns
from src.constants.months import Month


Graphs.show_cumulative_plot(
    GameTitle.STREET_FIGHTER_6, 
    SteamChartsColumns.AVG_PLAYERS, 
    Period(2024, Month.JANUARY, 24)
)