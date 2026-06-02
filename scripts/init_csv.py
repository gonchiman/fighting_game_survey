import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from src.constants.game_titles import GameTitle
from src.data.to_csv import ToCSV


for game_title in GameTitle:
    ToCSV.to_csv(game_title)