# *******************
# DE TEXTO A MARKDOWN
# *******************
import filecmp
from pathlib import Path


def run(text_path: Path) -> bool:
    markdown_lines = []

    with open(text_path, 'r') as txt_file:
        for line in txt_file:
            depth = line.count('\t')
            line = line.lstrip('\t')
            md_line = '#' * min(depth + 1, 6) + ' ' + line
            markdown_lines.append(md_line)
        
    md_path = 'data/txt2md/outline.md'
    with open(md_path, 'w') as md_file:
        md_file.write('\n'.join(markdown_lines))

    return filecmp.cmp(md_path, 'data/txt2md/.expected', shallow=False)


if __name__ == '__main__':
    run('data/txt2md/outline.txt')