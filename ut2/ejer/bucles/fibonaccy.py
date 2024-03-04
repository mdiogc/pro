number = int(input('Introduzca un número'))
first_serie = number - 1
second_serie = number - 2
fibonacci = first_serie + second_serie

for _ in range(100):
    print(fibonacci)
