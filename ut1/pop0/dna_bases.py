# ********************
# EN LAS BASES DEL ADN
# ********************


def run(dna: str) -> tuple:
    chromosome_A = float(dna.find('A'))
    chromosome_G = float(dna.find('G'))
    chromosome_T = float(dna.find('T'))
    chromosome_C = float(dna.find('C'))
    adenines_rate = chromosome_A
    guanines_rate = chromosome_G
    thymines_rate = chromosome_T
    cytosines_rate = chromosome_C
    return adenines_rate, guanines_rate, thymines_rate, cytosines_rate


if __name__ == '__main__':
    run('GGTTACCAACCCAGTCGAAAATTTGGTCAGGG')
