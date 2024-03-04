# ****************************************
# INTERCAMBIAR CLAVE-VALOR EN DICCIONARIOS
# ****************************************


def run(data: dict) -> dict:
    swapped_data = {}
    for key, value in data.items():
        if value in swapped_data:
            swapped_data[value] = max(swapped_data[value], key)
        else:
            swapped_data[value] = key

    return swapped_data


if __name__ == '__main__':
    run({'a': 1, 'b': 2, 'c': 3})
