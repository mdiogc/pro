# ********************
# DESPLAZANDO LA VOCAL
# ********************


def run(target_vowel: str, target_offset: int, input_text: str) -> str:
    output_text = input_text.find(target_vowel)

    return output_text


if __name__ == '__main__':
    run('e', 2, 'diferencia')
