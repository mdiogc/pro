import re


def extract_vowel_words(text: str) -> list[str]:
    vocals = r'\b[aeiouAEIOUáéíóúÁÉÍÓÚ]\w+'
    return re.findall(vocals, text)
