# ********************************
# UNA MÉTRICA PARA CADENA DE TEXTO
# ********************************


def run(text: str) -> int:
    numbers_of_letter = len(text)
    vocal = text.count('a')
    vocal2 = text.count('e')
    vocal3 = text.count('i')
    vocal4 = text.count('o')
    vocal5 = text.count('u')
    numbers_of_vocals = vocal + vocal2 + vocal3 + vocal4 + vocal5
    metric = numbers_of_letter * numbers_of_vocals

    return metric


if __name__ == '__main__':
    run('ordenador')
