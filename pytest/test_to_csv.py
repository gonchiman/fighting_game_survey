from src.data.to_csv import ToCSV
from src.constants.game_titles import GameTitle


def test__get_df():
    df = ToCSV._get_df(GameTitle.STREET_FIGHTER_6)

    assert not df.empty