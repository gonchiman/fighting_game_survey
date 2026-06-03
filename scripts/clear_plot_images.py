import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from src.constants.paths import PLOT_IMAGES_DIR
from src.utils.delete_all_files import delete_all_files


delete_all_files(PLOT_IMAGES_DIR)