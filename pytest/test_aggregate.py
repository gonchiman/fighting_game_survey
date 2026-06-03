from types import SimpleNamespace

import pandas as pd

from src.constants.columns import SteamChartsColumns
from src.data import aggregate


def test_create_total_analysis_df(monkeypatch):
    game_a = SimpleNamespace(title="Game A")
    game_b = SimpleNamespace(title="Game B")

    def fake_load_game_avg_players_df(game_title):
        if game_title == game_a:
            return pd.DataFrame(
                {
                    "Date": pd.to_datetime(
                        ["January 2024", "February 2024"],
                        format="%B %Y",
                    ),
                    "Game A": [10.0, 20.0],
                }
            )

        return pd.DataFrame(
            {
                "Date": pd.to_datetime(
                    ["February 2024", "March 2024"],
                    format="%B %Y",
                ),
                "Game B": [30.0, 40.0],
            }
        )

    monkeypatch.setattr(aggregate, "GameTitle", [game_a, game_b])
    monkeypatch.setattr(
        aggregate,
        "load_game_avg_players_df",
        fake_load_game_avg_players_df,
    )

    df = aggregate.create_total_analysis_df()

    assert df.columns.tolist() == [
        "Date",
        "Game A",
        "Game B",
        "Total Avg. Players",
        "Hours in Month",
        "Estimated Play Hours",
        "Cumulative Estimated Play Hours",
        SteamChartsColumns.MONTH,
    ]

    expected = pd.DataFrame(
        {
            "Date": pd.to_datetime(
                ["January 2024", "February 2024", "March 2024"],
                format="%B %Y",
            ),
            "Game A": [10.0, 20.0, 0.0],
            "Game B": [0.0, 30.0, 40.0],
            "Total Avg. Players": [10.0, 50.0, 40.0],
            "Hours in Month": [744, 696, 744],
            "Estimated Play Hours": [7440.0, 34800.0, 29760.0],
            "Cumulative Estimated Play Hours": [7440.0, 42240.0, 72000.0],
            SteamChartsColumns.MONTH: [
                "January 2024",
                "February 2024",
                "March 2024",
            ],
        }
    )

    pd.testing.assert_frame_equal(df, expected)
