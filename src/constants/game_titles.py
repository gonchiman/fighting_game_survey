from dataclasses import dataclass
from enum import Enum
from pathlib import Path

from src.constants.paths import DATA_GAMES_DIR


SAVE_DIR = DATA_GAMES_DIR


@dataclass(frozen=True)
class GameData:
    title: str
    app_id: int
    csv_path: Path


class GameTitle(Enum):
    STREET_FIGHTER_V = GameData(
        "Street Fighter V",
        310950,
        SAVE_DIR / "street_fighter_v.csv"
    )

    TEKKEN_7 = GameData(
        "TEKKEN 7",
        389730,
        SAVE_DIR / "tekken_7.csv"
    )

    DRAGON_BALL_FIGHTERZ = GameData(
        "DRAGON BALL FighterZ",
        678950,
        SAVE_DIR / "dragon_ball_fighterz.csv"
    )

    SOULCALIBUR_VI = GameData(
        "SOULCALIBUR VI",
        544750,
        SAVE_DIR / "soulcalibur_vi.csv"
    )

    MORTAL_KOMBAT_11 = GameData(
        "Mortal Kombat 11",
        976310,
        SAVE_DIR / "mortal_kombat_11.csv"
    )

    GUILTY_GEAR_STRIVE = GameData(
        "GUILTY GEAR -STRIVE-",
        1384160,
        SAVE_DIR / "guilty_gear_strive.csv"
    )

    THE_KING_OF_FIGHTERS_XV = GameData(
        "THE KING OF FIGHTERS XV",
        1498570,
        SAVE_DIR / "the_king_of_fighters_xv.csv"
    )

    STREET_FIGHTER_6 = GameData(
        "Street Fighter 6",
        1364780,
        SAVE_DIR / "street_fighter_6.csv"
    )

    MORTAL_KOMBAT_1 = GameData(
        "Mortal Kombat 1",
        1971870,
        SAVE_DIR / "mortal_kombat_1.csv"
    )

    GRANBLUE_FANTASY_VERSUS_RISING = GameData(
        "Granblue Fantasy Versus: Rising",
        2157560,
        SAVE_DIR / "granblue_fantasy_versus_rising.csv"
    )

    TEKKEN_8 = GameData(
        "TEKKEN 8",
        1778820,
        SAVE_DIR / "tekken_8.csv"
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