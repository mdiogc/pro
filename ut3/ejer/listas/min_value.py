# ************
# VALOR MÍNIMO
# ************


def run(values: list) -> int:
    min_value = values[0]
    for number in values:
        if number < min_value:
            min_value = number
    return min_value


if __name__ == '__main__':
    run([-11, 10, -6, 15, -1])
