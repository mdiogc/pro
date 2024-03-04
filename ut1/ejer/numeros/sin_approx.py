# *******************
# APROXIMANDO EL SENO
# *******************


def run(x: float) -> float:
    calcu = 180 - x

    sin = 4 * x * calcu / (40500 - x * calcu)

    return sin


if __name__ == '__main__':
    run(90)
