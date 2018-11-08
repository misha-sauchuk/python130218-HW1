"""Дано натуральное число N. Выведите все его цифры по одной, в обратном порядке, разделяя их пробелами или новыми
строками. При решении этой задачи нельзя использовать строки, списки, массивы (ну и циклы, разумеется).
Разрешена только рекурсия и целочисленная арифметика.
"""


# Function to input a data
def input_data():
    """Input data and return a string"""
    data = input('Please, enter a number:')
    return data


# Function to change string to int
def inp_num():
    """Input data return in int"""
    while True:
        try:
            num = int(input_data())
            if num < 0:
                print('Invalid input')
                continue
            return num
        except:
            print('Invalid input')
            continue


# function to calculate the sum of digits in number
def print_reverse(nat_num):
    digit = nat_num % 10
    nat_num = nat_num // 10
    print(digit, end=' ')
    if nat_num:
        print_reverse(nat_num)


# ask user to input number
number = inp_num()


def test_inp_num():
    if type(number) is int:
        print('\ntest inp_num is OK')


test_inp_num()
