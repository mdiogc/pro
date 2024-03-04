# ********************
# UNA SENCILLA FUNCIÓN
# ********************


def run(a: int, b: int) -> float:
    F = round(a**2 + b**2 - (a * b) ** 0.5, 7)

    return F


if __name__ == '__main__':
    run(5, 7)
