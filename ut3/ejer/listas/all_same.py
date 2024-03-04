# *****************************
# SOMOS IGUALES, PERO DISTINTOS
# *****************************


def run(items: list) -> bool:
    for the_truth in items:
        if the_truth == items:
            all_same = True
        else:
            all_same = False

    return all_same


if __name__ == '__main__':
    run([1, 1, 1, 1, 1, 1])
