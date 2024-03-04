# ********************
# LEYENDO FICHEROS CSV
# ********************
from pathlib import Path


def run(datafile: Path) -> list:
    file = open(datafile, 'r')
    for line in file:
        
    file.readline
    data = []

    return data


if __name__ == '__main__':
    run('data/read_csv/pokemon.csv')
