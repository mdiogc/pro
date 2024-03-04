# *********************
# DAME UN SLUG SENCILLO
# *********************


def run(text: str) -> str:
    VOCALS = 'a', 'e', 'i', 'o', 'u'
    vocals_with_marks = 'á', 'é', 'í', 'ó', 'ú'
    text_minuscule = text.lower()
    text_script = text_minuscule.replace('\n', '-')
    vocals_with_accent = text_script.replace(vocals_with_marks, VOCALS)
    slug = vocals_with_accent
    return slug


if __name__ == '__main__':
    run('hola probando')
