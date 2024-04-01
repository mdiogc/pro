# **********
# PALÍNDROMO
# **********


def is_palindrome(text: str) -> bool:
    text = text.replace(' ', '').upper()
    return text == text[::-1]

