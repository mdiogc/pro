name = input('Enter your name and surname here')


if name == name.title():
    solution_name = True
if name == name.lower():
    solution_name = 'Error. You must write it correctly'
if name == name.upper():
    solution_name = 'Error. You must write it correctly'
if name == name.capitalize():
    solution_name = 'Error. You must write it correctly'
if name == name.swapcase():
    solution_name = 'Error. You must write it correctly'


print(solution_name)
