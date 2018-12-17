import pytest
from pandas import read_table

from main import target_with_smallest_interval, Url, Headers


class TestSmallestInterval:
    @pytest.fixture
    def weather_data(self):
        weather_data = read_table(Url.WEATHER, r'\s+')

        return weather_data

    @pytest.fixture
    def football_data(self):
        football_headers_names = ['Index', 'Team', 'P', 'W', 'L', 'D', 'F', '-', 'A', 'Pts']
        football_data = read_table(Url.FOOTBALL, r'\s+', names=football_headers_names)

        return football_data

    def test_correct_weather_result(self, weather_data):
        day = target_with_smallest_interval(
                weather_data,
                Headers.Weather.MAX_TEMPERATURE,
                Headers.Weather.MIN_TEMPERATURE,
                Headers.Weather.DAY_NUMBER
        )
        assert day == '14'

    def test_correct_football_result(self, football_data):
        team = target_with_smallest_interval(
                football_data,
                Headers.Football.GOALS_FOR,
                Headers.Football.GOALS_AGAINST,
                Headers.Football.TEAM_NAME
        )
        assert team == 'Aston_Villa'
