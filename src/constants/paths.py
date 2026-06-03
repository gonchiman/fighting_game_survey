from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "data"
DATA_GAMES_DIR = DATA_DIR / "games"
DATA_TOTAL_ANALYSIS_DIR = DATA_DIR / "total_analysis"

PLOT_IMAGES_DIR = BASE_DIR / "plot_images"
PLOT_IMAGES_GAMES_DIR = PLOT_IMAGES_DIR / "games"
PLOT_IMAGES_TOTAL_ANALYSIS_DIR = PLOT_IMAGES_DIR / "total_analysis"