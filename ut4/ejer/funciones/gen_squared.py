# *******************
# GENERANDO CUADRADOS
# *******************


def gen_sq(n: int) -> list:
    numbers = (n**2 for n in range(0, n))
    squared = list(numbers)
    return squared
