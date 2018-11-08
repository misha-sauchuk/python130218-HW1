"""Реализовать программу с базой учащихся группы (данные хранятся в файле).
Записи по учащемуся должны быть представлены отдельным классом с полями: имя, фамилия, пол, возраст.
Программа должна предусматривать поиск по одному или нескольким полям базы. Результат выводить в удобочитаемом виде
с порядковым номером записи. Скрипт программы должен принимать параметр, который определяет формат хранения и
реализации БД: в текстовом файле с определенной структурой; в файле json."""

import json


# create a class with method to find students according to the search mask
class Finder:
    def __init__(self):
        self.dict_check = {'name': '', 'surname': '', 'sex': '', 'age': ''}  # create a dictionary with empty values
        self.dict_check = self.search_info()  # Ask function search_info

    def search_info(self):  # function to input information to search
        for key in self.dict_check.keys():
            print('Please, enter an information about {}, or press "Enter" to skip:'.format(key.upper()))
            self.dict_check[key] = input()
        return self.dict_check

    def find(self):
        find_numbers = 0  # count how many parameters we use to search the student
        for value in self.dict_check.values():
            if value: find_numbers += 1
        number = 0  # check if there are students in our list with input information
        for dic in self.stud_dict:
            if dic.items() & self.dict_check.items() and len(dic.items() & self.dict_check.items()) == find_numbers:
                number += 1
                print('{}. {} {}, {} years old, {}'.format(number, dic['surname'], dic['name'], dic['age'], dic['sex']))

        if number == 0:  # print result if there is no coincidence
            print('There are no students with input data')


# create a subclass that will modify data from file.txt  to the view of search mask
class TextFile(Finder):
    def __init__(self):
        super().__init__()
        with open(file_name) as text_file:
            self.stud_list = [line.rstrip().split() for line in text_file]
        keys = ['surname', 'name', 'sex', 'age']
        self.stud_dict = [dict(zip(keys, values)) for values in self.stud_list]


# create a subclass that will modify data from file.json  to the view of search mask
class JsonFile(Finder):
    def __init__(self):
        super().__init__()
        self.stud_dict = []
        with open(file_name) as json_file:
            for line in json_file:
                self.stud_dict.append(json.loads(line))


type_files = {'txt': TextFile, 'json': JsonFile}  # dict with key as filename extension and value as subclass name
while True:  # circle to input file name and run the find procedure
    file_name = input('Please, input the file name or "Q" to quit:\n')
    if file_name.upper() == 'Q':
        break
    file_name_list = file_name.split('.')
    file_to_do = type_files.get(file_name_list[-1])  # check if if file type is supported by module
    if file_to_do is None:
        print('This file type is not supported\n Please, use only .txt ot .json files')
        continue
    else:
        file_to_do = file_to_do()  # create an instance of subclass
        file_to_do.find()  # run the method of instance
