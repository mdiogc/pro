# ******************
# DISTANCIA EUCLÍDEA
# ******************


def run(x1: float, y1: float, x2: float, y2: float) -> float:
    unknow_fuction = (x2 - x1) ** 2
    second_fuction = (y2 - y1) ** 2
    distance = (unknow_fuction + second_fuction) ** 0.5

    return distance


if __name__ == '__main__':
    run(3, 5, -7, -4)
