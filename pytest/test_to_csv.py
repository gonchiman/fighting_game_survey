from types import SimpleNamespace

import pandas as pd

from src.data.to_csv import ToCSV
from src.constants.game_titles import GameTitle


def test__get_df():
    df = ToCSV._get_df(GameTitle.STREET_FIGHTER_6)

    assert not df.empty


def test_to_csv(monkeypatch, tmp_path):
    csv_path = tmp_path / "test.csv"
    game_title = SimpleNamespace(csv_path=csv_path)

    monkeypatch.setattr(
        ToCSV,
        "_get_df",
        lambda game_title: pd.DataFrame({"title": ["Street Fighter 6"]}),
    )

    ToCSV.to_csv(game_title)

    assert csv_path.exists()
