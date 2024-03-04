# ****************
# EL CUADRADO ROJO
# ****************


def run(arc_A: float) -> float:
    PI = 3.14
    perimeter = arc_A * 4
    radius = perimeter / (2 * PI)

    area = round(radius**2, 10)

    return area


if __name__ == '__main__':
    run(1)
