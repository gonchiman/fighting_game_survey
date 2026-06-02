import matplotlib.pyplot as plt

from src.constants.columns import SteamChartsColumns
from src.constants.game_titles import GameTitle
from src.graphs.graphs import Graphs
from src.entities.period import Period
from src.constants.months import Month


def test_plot(monkeypatch):
    monkeypatch.setattr(plt, "show", lambda: None)

    Graphs.show_plot(
        game_title=GameTitle.STREET_FIGHTER_6,
        column=SteamChartsColumns.AVG_PLAYERS,
        period=None,
        save=False
    )

    plt.close("all")


def test_plot_with_period(monkeypatch):
    monkeypatch.setattr(plt, "show", lambda: None)

    period = Period(start_year=2024, start_month=Month.JANUARY, duration=12)

    Graphs.show_plot(
        game_title=GameTitle.STREET_FIGHTER_6,
        column=SteamChartsColumns.AVG_PLAYERS,
        period=period,
        save=False
    )

    plt.close("all")


def test_plot_with_save_mode(monkeypatch):
    monkeypatch.setattr(plt, "savefig", lambda *args, **kwargs: None)

    Graphs.show_plot(
        game_title=GameTitle.STREET_FIGHTER_6,
        column=SteamChartsColumns.AVG_PLAYERS,
        period=None,
        save=True
    )

    plt.close("all")


def test_cumulative_plot(monkeypatch):
    monkeypatch.setattr(plt, "show", lambda: None)

    Graphs.show_cumulative_plot(
        game_title=GameTitle.STREET_FIGHTER_6,
        column=SteamChartsColumns.AVG_PLAYERS,
        period=None,
        save=False
    )

    plt.close("all")


def test_cumulative_play_hours_plot(monkeypatch):
    monkeypatch.setattr(plt, "show", lambda: None)

    Graphs.show_cumulative_play_hours_plot(
        game_title=GameTitle.STREET_FIGHTER_6,
        period=None,
        save=False
    )

    plt.close("all")