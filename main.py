from pandas import read_table, DataFrame, to_numeric


class Url:
    WEATHER = 'http://codekata.com/data/04/weather.dat'
    FOOTBALL = 'http://codekata.com/data/04/football.dat'


class Headers:
    class Weather:
        MAX_TEMPERATURE = 'MxT'
        MIN_TEMPERATURE = 'MnT'
        DAY_NUMBER = 'Dy'

    class Football:
        GOALS_FOR = 'F'
        GOALS_AGAINST = 'A'
        TEAM_NAME = 'Team'


def target_with_smallest_interval(input: DataFrame, minuend: str, subtrahend: str, target: str) -> str:
    diff = to_numeric(input[minuend], errors='coerce') - to_numeric(input[subtrahend], errors='coerce')

    return input[target][diff.abs().idxmin()]


def run():
    weather_data = read_table(Url.WEATHER, r'\s+')

    football_headers_names = ['Index', 'Team', 'P', 'W', 'L', 'D', 'F', '-', 'A', 'Pts']
    football_data = read_table(Url.FOOTBALL, r'\s+', names=football_headers_names)

    day = target_with_smallest_interval(
            weather_data,
            Headers.Weather.MAX_TEMPERATURE,
            Headers.Weather.MIN_TEMPERATURE,
            Headers.Weather.DAY_NUMBER
    )

    team = target_with_smallest_interval(
            football_data,
            Headers.Football.GOALS_FOR,
            Headers.Football.GOALS_AGAINST,
            Headers.Football.TEAM_NAME
    )

    print(f'The smallest temperature spread was on day [{day}]')
    print(f'Team with the smallest difference in for and against goals is [{team}]')


if __name__ == '__main__':
    run()
