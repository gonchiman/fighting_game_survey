import pandas as pd

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from src.constants.months import Month
from src.constants.columns import TotalAnalysisColumns
from src.constants.paths import DATA_TOTAL_ANALYSIS_DIR


df = pd.read_csv(
    DATA_TOTAL_ANALYSIS_DIR / "total_fighting_games_analysis.csv",
    encoding="utf-8-sig",
)

pivot = f"{Month.MAY} 2023"
pivot_index = df[df[TotalAnalysisColumns.MONTH] == pivot].index

df1 = df[df.index < pivot_index[0]]
df2 = df[df.index >= pivot_index[0]]

print("Mean before pivot:", df1[TotalAnalysisColumns.ESTIMATED_PLAY_HOURS].mean())
print("Mean after pivot:", df2[TotalAnalysisColumns.ESTIMATED_PLAY_HOURS].mean())