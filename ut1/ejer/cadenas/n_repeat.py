# *************
# SUMA REPETIDA
# *************


def run(n: int) -> int:
    number = n
    result = number + number**2 + number**3

    return result


if __name__ == '__main__':
    run(3)
