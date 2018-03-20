"""Реализовать программу, которая выводит содержимое каталога в файловой системе.
Путь к каталогу запрашивается у пользователя.
"""
import os

# open file where we will store info
file_to_save = open('dirs.txt', 'w')
home_path = input('Please, enter a path to your dir:\n')
if not home_path:
    home_path = os.getcwd()


# function to go through all folders in user dir and take all files
def search_file(path):
    os.chdir(path)
    for item in os.listdir(path):
        if os.path.isfile(item):
            file_to_save.write(item + '\n')
        if os.path.isdir(item):
            path = os.path.abspath(item)
            search_file(path)
            os.chdir(path + '/..')


search_file(home_path)
