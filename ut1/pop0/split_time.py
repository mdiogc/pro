# *******************
# SEPARANDO EL TIEMPO
# *******************


def run(seconds: int) -> tuple:
    hours_to_seconds = 3600
    minutes_to_seconds = 60
    hours = seconds // hours_to_seconds
    minutes = seconds // hours_to_seconds % minutes_to_seconds
    seconds = seconds % minutes_to_seconds
    return hours, minutes, seconds


if __name__ == '__main__':
    run(31256)
