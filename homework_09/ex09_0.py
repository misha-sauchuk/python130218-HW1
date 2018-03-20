"""Дано натуральное число N. Вычислите сумму его цифр.
При решении этой задачи нельзя использовать строки, списки, массивы и циклы."""


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
        except ValueError as er:
            print('Value Error: ', er)
            continue


# function to calculate the sum of digits in number
def count_sum(nat_num=None, count=0):
    if nat_num is None:
        nat_num = inp_num()
    digit = nat_num % 10
    nat_num = nat_num // 10
    count = count + digit
    if nat_num:
        count_sum(nat_num, count)
    else:
        print('The sum of digits in your number is {}'.format(count))
        request_to_exit = input('Please, press "Y" to exit or press "Enter" to continue: ')
        if request_to_exit.upper() == 'Y' or request_to_exit.upper() == 'YES':
            return
        else:
            count_sum()


# call the function to calculate the sum of digits in number
count_sum()


def test_inp_num():
    number = inp_num()
    if type(number) is int:
        print('test inp_num is OK')


def test_count_sum():
    if count_sum(nat_num=123) == 6:
        print('test count_sum is OK')


test_inp_num()
#test_count_sum()
