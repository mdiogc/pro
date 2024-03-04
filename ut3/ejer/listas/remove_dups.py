# *********************
# ELIMINANDO DUPLICADOS
# *********************


def run(nums_dups: list) -> list:
    nums_unique = []
    for number_repeat in nums_dups:
        if number_repeat not in nums_unique:
            nums_unique.append(number_repeat)

    return nums_unique


if __name__ == '__main__':
    run([2, 3, 2, 2, 1, 5, 4, 2, 4, 9])
