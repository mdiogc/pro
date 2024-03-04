# *******************************
# ADIVINANDO PERSONAJES DE MARVEL
# *******************************


def run(can_fly: bool, is_human: bool, has_mask: bool) -> str:
    if can_fly and is_human and has_mask:
        character = 'Ironman'
        if not is_human and has_mask:
            character = 'Ronan Accuser'
        else:
            character = 'Vision'
    else:
        character = 'Captain Marvel'

    if not can_fly and is_human and has_mask:
        character = 'Spiderman'
    else:
        character = 'Hulk'

    return character


if __name__ == '__main__':
    run(True, True, True)
