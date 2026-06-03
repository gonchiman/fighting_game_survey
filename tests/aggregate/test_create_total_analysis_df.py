import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(BASE_DIR))

from src.data.aggregate import create_total_analysis_df


print(create_total_analysis_df().columns.tolist())