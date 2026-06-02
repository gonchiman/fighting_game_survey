from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from src.constants.paths import DATA_DIR

@dataclass(frozen=True)
class GameData:
    title: str
    app_id: int
    csv_path: Path


class GameTitle(Enum):
    STREET_FIGHTER_6 = GameData(
        "Street Fighter 6",
        1364780,
        DATA_DIR / "street_fighter_6.csv"
    )

    @property
    def title(self) -> str:
        return self.value.title

    @property
    def app_id(self) -> int:
        return self.value.app_id

    @property
    def csv_path(self) -> Path:
        return self.value.csv_path