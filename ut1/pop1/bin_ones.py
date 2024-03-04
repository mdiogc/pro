# ***************************
# LOS UNOS CUENTAN EN BINARIO
# ***************************


def run(number: int) -> int:
    bynary_of_a_number = bin(number)
    count_ones = bynary_of_a_number.count('1')

    return count_ones


if __name__ == '__main__':
    run(99)
