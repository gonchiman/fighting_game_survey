import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(BASE_DIR))

from src.data.to_csv import ToCSV
from src.constants.game_titles import GameTitle


df = ToCSV._get_df(GameTitle.STREET_FIGHTER_6)
print(df)