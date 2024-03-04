# *********************
# CONTANDO MILISEGUNDOS
# *********************


def run(hours: int, minutes: int, seconds: int) -> float:
    hours_to_ms = hours * 3_600_000
    minutes_to_ms = minutes * 60000
    seconds_to_ms = seconds * 1000
    time_since_midnight = hours_to_ms + minutes_to_ms + seconds_to_ms

    return time_since_midnight


if __name__ == '__main__':
    run(0, 1, 1)
