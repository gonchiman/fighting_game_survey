from dataclasses import dataclass
from pathlib import Path
from src.constants.paths import STREET_FIGHTER_6_CSV_PATH

@dataclass(frozen=True)
class GameData:
    title: str
    app_id: int
    csv_path: Path


class GameTitle:
    STREET_FIGHTER_6 = GameData(
        "Street Fighter 6", 
        1364780, 
        STREET_FIGHTER_6_CSV_PATH
    )