# *******************
# HEXADECIMAL A TEXTO
# *******************


def run(hex_codes: list) -> str:
    text = ''.join(chr(int(items, 16)) for items in hex_codes)
    return text


if __name__ == '__main__':
    run(['1f49a', '2728', '1f389', '1f3c6'])
