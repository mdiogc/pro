# *******************
# TEMPERATURAS MEDIAS
# *******************
import filecmp
from pathlib import Path


def run(input_path: Path) -> bool:
    output_path = 'data/avg_temps/avg_temps.dat'
    with open(input_path, 'r') as input_file:
        data = input_file.readlines()


    monthly_avg_temps = []
    for line in data:
        temperatures = list(map(float, line.strip().split()))
        monthly_avg = sum(temperatures) / len(temperatures)
        monthly_avg_temps.append(monthly_avg)

    with open(output_path, 'w') as output_file:
        for temp in monthly_avg_temps:
         output_file.write(f"{temp:.2f}\n")

    return filecmp.cmp(output_path, 'data/avg_temps/.expected', shallow=False)


if __name__ == '__main__':
    run('data/avg_temps/temperatures.dat')