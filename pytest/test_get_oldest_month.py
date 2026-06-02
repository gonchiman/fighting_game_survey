from src.constants.game_titles import GameTitle
from src.data.get_oldest_month import get_oldest_month


def test_get_oldest_month():
    game_title = GameTitle.STREET_FIGHTER_6
    oldest_month = get_oldest_month(game_title)

    assert oldest_month == "June 2023"