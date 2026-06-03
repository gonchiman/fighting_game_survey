import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from src.constants.paths import PLOT_IMAGES_TOTAL_ANALYSIS_DIR
from src.graphs.graphs import Graphs
from src.utils.delete_all_files import delete_all_files


delete_all_files(PLOT_IMAGES_TOTAL_ANALYSIS_DIR)

Graphs.total_cumulative_play_hours_plot(save=True)