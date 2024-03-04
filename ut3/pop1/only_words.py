# **********
# ONLY WORDS
# **********


def run(items: list) -> int:
    sum_words = sum(len(item) for item in items if isinstance(item, str))

    return sum_words


if __name__ == '__main__':
    run([99, 'x', 3, 5, 'hello', 'banana', 4])
