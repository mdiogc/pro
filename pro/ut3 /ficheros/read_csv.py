# ********************
# LEYENDO FICHEROS CSV
# ********************
from pathlib import Path


def run(datafile: Path) -> list:
    data = []
    with open(datafile, 'r', newline='') as csvfile:
        lines = csvfile.readlines()
        headers = lines[0].strip().split(',')
        for line in lines[1:]:
            row = {}
            values = line.strip().split(',')
            for header, value in zip(headers, values):
                if value.lower() == "true":
                    row[header] = True
                elif value.lower() == "false":
                    row[header] = False
                elif value.isdigit():
                    row[header] = int(value)
                else:
                    row[header] = value
            data.append(row)

    return data


if __name__ == '__main__':
    run('data/read_csv/pokemon.csv')