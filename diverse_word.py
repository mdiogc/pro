# ***************
# PALABRA DIVERSA
# ***************


def run(words: list) -> str:
    max_letters = 0
    #dword = ''.join(len(set(word))for word in words if letters > max_letters)

    for word in words:
        letters = len(set(word))
        if letters > max_letters:
            max_letters = letters
            dword = word

    return dword


if __name__ == '__main__':
    run(['dictionary', 'turtle', 'flexibility', 'humanity'])