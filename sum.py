def add(numbers):

    result = 0
    for number in numbers:
        result += number
    return result


my_numbers = [4, 7, 2, 8]
if sum(my_numbers) == add(my_numbers):
    print('Lo hice bien!')
else:
    print('Lo hice mal!')
print(add(my_numbers))
