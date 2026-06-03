import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(BASE_DIR))

from src.graphs.graphs import Graphs


Graphs.total_cumulative_play_hours_plot(save=False)