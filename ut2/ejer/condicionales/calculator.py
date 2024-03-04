value1 = int(input('Enter first number: '))
value2 = int(input('Enter second number: '))
sign = input('Enter the operation symbol: ')


match sign:
    case '+':
        result = value1 + value2
    case '-':
        result = value1 - value2
    case '*':
        result = value1 * value2
    case '//':
        result = value1 // value2
    case _:
        result = None
        print('Unkown result')

print(f'{value1}{sign}{value2} = {result}')
