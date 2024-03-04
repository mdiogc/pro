# *************************
# SIMULANDO EL COMANDO HEAD
# *************************
from pathlib import Path


def run(file: Path, n: int) -> str:
    with open(file) as text:
        for line in text:
            


    lines = 'output'

    return lines


if __name__ == '__main__':
    run('data/head/nba_season22.txt', 3)
