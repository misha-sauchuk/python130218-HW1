"""Реализовать программу, позволяющую осуществлять управление файлами: копирование, создание, удаление, переименование.
Необходимо предусмотреть возможность смен директории.
Изначально используется текущий каталог запуска скрипта программы."""

import os
import shutil


def file_to_do():
    while True:
        file = input()
        home_path = input('Please, enter a path to your file:\n')

        if not home_path:
            pass
        else:
            home_path = os.chdir(home_path)
        if file in os.listdir():
            file_path = os.path.abspath(file)
        else:
            print('There is no such file. Please, try again')
            continue
        return file_path


def new_folder():
    new_path = input('Please, enter a new path to your file:\n')
    return new_path


def copy_file():
    print('Please, enter the name of the file to copy:')
    shutil.copy(r'{}'.format(file_to_do()), r'{}'.format(new_folder()))


def create_file(file_name, file_folder):
    os.chdir(file_folder)
    with open(file_name, 'w') as user_file:
        pass


def del_file():
    print('Please, enter the name of the file your would like to delete:')
    file_path = file_to_do()
    os.remove(file_path)


def rename_file():
    print('Please, enter the name of the file your would like to rename:')
    file_path = file_to_do()
    new_name = input('Please, enter a new name of file:\n')
    os.rename(file_path, new_name)


while True:
    what_to_do = input('Please, enter the number of operation you would like to do:\n'
                       '1. create\n'
                       '2. copy\n'
                       '3. delete\n'
                       '4. rename\n'
                       '5. quit\n')
    if what_to_do[0] == '1' or what_to_do == 'create':
        create_file(input('Please, enter the name of a new file:\n'), new_folder())
        print('ok')
    elif what_to_do[0] == '2' or what_to_do == 'copy':
        copy_file()
        print('ok')
    elif what_to_do[0] == '3' or what_to_do == 'delete':
        del_file()
        print('ok')
    elif what_to_do[0] == '4' or what_to_do == 'rename':
        rename_file()
        print('ok')
    elif what_to_do[0] == '5' or what_to_do == 'quit':
        print('byu')
        quit()
