# ****************
# CONTANDO COMO WC
# ****************
from pathlib import Path


def run(input_path: Path) -> tuple:
   with open(input_path, 'r', encoding='utf-8') as archive:
        num_lines = 0
        num_words = 0
        num_bytes = 0

        for line in archive:
            num_lines += 1
            num_words += len(line.split())
            num_bytes += len(line.encode('utf-8'))

    
        return num_lines, num_words, num_bytes


if __name__ == '__main__':
    run('data/wc/lorem.txt')