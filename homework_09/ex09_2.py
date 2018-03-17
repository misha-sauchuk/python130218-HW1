"""Реализовать программу с базой учащихся группы (данные хранятся в файле). Записи по учащемуся: имя, фамилия, пол,
возраст. Программа должна предусматривать поиск по одному или нескольким полям базы. Результат выводить в
удобочитаемом виде с порядковым номером записи. Скрипт программы должен принимать параметр, который определяет
формат хранения и реализации БД: в текстовом файле с определенной структурой; в файле json."""

import json
from HomeWork_05.ex5_03 import find_stud

# read data from database_file in format where elements are dict
stud_list = []
with open('stud_db.js') as db:
    for line in db:
        stud_list.append(json.loads(line))

# with circle found needful information
while True:
    find_stud(stud_list)
    request = input('Do yob want to continue? Y/N')
    if request == 'N' or request == 'n':
        quit()
