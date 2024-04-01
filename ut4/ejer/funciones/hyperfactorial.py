# **************
# HIPERFACTORIAL
# **************


def hyperfactorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        temp = i
        for _ in range(1, i):
            temp *= i
        result *= temp
    return result
