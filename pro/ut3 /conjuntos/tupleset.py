# ******************
# TUPLAS Y CONJUNTOS
# ******************


def run(input: tuple) -> set:
    firstset = set()
    secondset = set()
    for item in input:
        firstset.add(item[0])
        secondset.add(item[1])
    output = (firstset, secondset)

    return output


if __name__ == '__main__':
    run(((4, 3), (8, 2), (7, 5), (8, 2), (9, 1)))