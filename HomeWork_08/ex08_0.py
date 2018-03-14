"""Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
Окончанием ввода пусть служит пустая строка."""

# open a file
text_file = open('text_file.txt', 'a')

# circle to ad data to the file
while True:
    str = input('Please, enter a string: ')
    if not str:
        text_file.close()
        break
    str = str + '\n'
    text_file.write(str)

