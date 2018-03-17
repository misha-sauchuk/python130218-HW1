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
        except:
            print('Invalid input')
            continue


# function to calculate the sum of digits in number
def count_sum(nat_num):
    digit = nat_num % 10
    nat_num = nat_num // 10
    global count
    count = count + digit
    if nat_num:
        count_sum(nat_num)
    return count


# ask user to input number
while True:
    number = inp_num()
    count = 0
    answer = count_sum(number)
    print('The summ of digits in {} is {}'.format(number, answer))
    request_to_exit = input('Do you want to exit? Y/N ')
    if request_to_exit.upper() == 'Y' or request_to_exit.upper() == 'YES':
        count = 0
        break


def test_inp_num():
    if type(number) is int:
        print('test inp_num is OK')


def test_count_sum():
    test = count_sum(123)
    if test == 6:
        print('test count_sum is OK')


test_inp_num()
test_count_sum()
