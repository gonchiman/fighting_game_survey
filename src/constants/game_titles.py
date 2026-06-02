from dataclasses import dataclass

@dataclass(frozen=True)
class GameData:
    title: str
    app_id: int


class GameTitle:
    STREET_FIGHTER_6 = GameData("Street Fighter 6", 1364780)