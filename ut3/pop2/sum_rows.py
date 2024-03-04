# *************
# SUMANDO FILAS
# *************
from pathlib import Path


def run(data_path: Path) -> tuple:
    with open(data_path, 'r') as file:
        lines = file.readlines()
        numbers = []
        for line in lines:
            row = [int(num) for num in line.strip().split()]
            numbers.append(row)
            rsum = tuple(sum(row) for row in numbers)

    return rsum


if __name__ == '__main__':
    run('data/sum_rows/data1.txt')
