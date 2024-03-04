import sys

values = sys.argv[1:]
values = [int(number) for number in values]

average_values = sum(values) / len(values)


print(f'La media de los números es: {average_values:.2f}')
