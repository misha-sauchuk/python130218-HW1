"""Написать программу, запрашивающую у пользователя строку с текстом и разделитель.
Необходимо вывести список слов с их длиной в начале слова, например, 5hello.
Для каждой из пользовательских функций написать функцию-тест."""


# Function to input a data
def input_data():
    """Input data and return a string"""
    inp_data = input()
    return inp_data


# Function to create a list from text using separator
def cr_lst(txt, separator):
    """Create list using separator"""
    txt_list = txt.split(separator)
    return txt_list


# Request to input data
print('Please, enter a text:')
text = input_data()
print('Please, enter a separator: ')
sep = input_data()

# Use function to create a list of words
words_list = cr_lst(text, sep)

# Circle to count the len of each word and change the list
count = 0
while count < len(words_list):
    words_list[count] = str(len(words_list[count])) + words_list[count]
    count += 1

print(words_list)


# Functional Test for function cr_lst
def func_test_cr_lst():
    txt = 'Monty Python'
    separator = ' '
    if cr_lst(txt, separator) == ['Monty', 'Python']:
        print('test ok')


func_test_cr_lst()
