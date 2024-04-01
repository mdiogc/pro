# *******************
# FIBONACCI GENERADOR
# *******************


def run(n: int) -> list:
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibo_sequence = run(n - 1)
        fibo_sequence.append(fibo_sequence[-1] + fibo_sequence[-2])
        return fibo_sequence
