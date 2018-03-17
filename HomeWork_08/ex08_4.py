"""Реализовать программу, которая выводит содержимое каталога в файловой системе.
Путь к каталогу запрашивается у пользователя.
"""
import os
file_to_save = open('dirs.txt', 'w')
home_path = input('Please, enter a path to your dir:\n')
if not home_path:
    home_path = os.getcwd()


def search_file(path):
    os.chdir(path)
    for file in os.listdir(path):
        if os.path.isfile(file):
            file_to_save.write(file + '\n')
    for dir in os.listdir(path):
        if os.path.isdir(dir):
            path = os.path.abspath(dir)
            search_file(path)
            os.chdir(path + '/..')


search_file(home_path)
