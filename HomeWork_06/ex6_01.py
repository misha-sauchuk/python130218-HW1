"""Написать программу нахождения простых чисел, используя решето Эратосфена.
   Для каждой из пользовательских функций написать функцию-тест.
"""


# Function to input a data
def input_data():
    """Input data and return a string"""
    inp_data = input()
    return inp_data


# Function to convert str to int and check the correct input
def inp_num():
    ''' Input data return in int'''
    while True:
        try:
            num = int(input_data())
            if num <= 2:
                print('Invalid input')
                continue
            else:
                return num
        except:
            print('Invalid input')
            continue


# Function to find prime numbers in user's list
def prime_number(lst):
    step = 2
    while step <= len(lst):
        for i in lst:
            if i / step != 1 and i % step == 0:
                lst.remove(i)
        step += 1
    return lst


# Create a list on numbers we would like to check
print('Please, enter last number:')
last_num = inp_num()
num_list = list(range(2, last_num + 1))

# Use function 'prime_number' to find all prime numbers in the list and print it
num_list = prime_number(num_list)
print('Prime numbers is {}'.format(num_list))


def test_prime_num():
    if prime_number([2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,20]) == [2, 3, 5, 7, 11, 13, 17, 19]:
        print('test ok')
test_prime_num()