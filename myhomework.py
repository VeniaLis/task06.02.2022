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


#3

my_operation = input('Введите действие (+,-,*,/): ')
my_number1 = int(input(''))
my_number2 = int(input(''))
def arithmetic(my_operation, my_number1, my_number2):
    if my_operation == '+':
        return my_number1 + my_number2
    elif my_operation == '-':
        return my_number1 - my_number2
    elif my_operation == '*':
        return my_number1 * my_number2
    elif my_operation == '/':
        return my_number1 / my_number2
    else:
        return 'Неизвестная операция'

print(arithmetic(my_operation, my_number1, my_number2))

#4
my_word = input('Введите слово: ')
my_word2 = my_word[::-1]


def my_solofunction(my_word, my_word2):
    if my_word == my_word2:
        return 'слово палиндроп'
    else:
        return 'не палиндроп'


print(my_solofunction(my_word, my_word2))