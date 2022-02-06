#1
from random import randint
def is_prime():
    my_list = int(input('Введите число: '))
    if my_list % 2 == 0:
        return True
    else:
        return False
print(is_prime())

#2
def square():
    my_square = int(input('Введите число: '))
    perimeter = my_square * 4
    plochad = my_square * my_square
    diaganal_square = my_square ** (0.5)
    result = (perimeter, plochad, diaganal_square)
    return result

print(square())