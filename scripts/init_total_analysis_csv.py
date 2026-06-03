import sys
from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from src.constants.paths import DATA_TOTAL_ANALYSIS_DIR
from src.utils.delete_all_files import delete_all_files
from src.data.aggregate import create_total_analysis_df


delete_all_files(DATA_TOTAL_ANALYSIS_DIR)

df = create_total_analysis_df()
df.to_csv(DATA_TOTAL_ANALYSIS_DIR / "total_fighting_games_analysis.csv", index=False, encoding="utf-8-sig")
df.to_excel(DATA_TOTAL_ANALYSIS_DIR / "total_fighting_games_analysis.xlsx", index=False, encoding="utf-8-sig")