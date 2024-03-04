name = str(input('Enter your name here'))


match name:
    case name.title():
        solution_name = True
    case name.lower():
        solution_name = 'Error. You must write it correctly'
    case name.capitalize():
        solution_name = 'Error. You must write it correctly'
    case name.upper():
        solution_name = 'Error. You must write it correctly'
    case name.swapcase():
        solution_name = 'Error. You must write it correctly'


print(solution_name)
