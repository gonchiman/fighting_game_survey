from src.constants.game_titles import GameTitle
from src.data.get_oldest_month_and_year import get_oldest_month_and_year


def test_get_oldest_month_and_year():
    game_title = GameTitle.STREET_FIGHTER_6
    oldest_month, oldest_year = get_oldest_month_and_year(game_title)

    assert oldest_month == "June"
    assert oldest_year == "2023"