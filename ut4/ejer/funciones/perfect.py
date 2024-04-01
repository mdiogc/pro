# *****************
# NÚMEROS PERFECTOS
# *****************


def matraca(n):
    '''
    Calcula los divisores de un número.
 
    
    '''
    divisor = []
    for i in range(1, n):
        if n % i == 0:
            divisor.append(i)
    return divisor

def is_perfect(n):
    divisors = matraca(n)
    sum_divisors = sum(divisors)
    return sum_divisors == n

