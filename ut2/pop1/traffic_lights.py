# ****************
# SE PONE EN VERDE
# ****************


def run(color: str) -> str:
    match color:
        case '🟢':
            new_color = '🟠'
        case '🟠':
            new_color = '🔴'
        case '🔴':
            new_color = '🟢'
        case _:
            new_color = 'Error. Introduce el emoji adecuado'

    return new_color


if __name__ == '__main__':
    run('🟢')
