"""Реализовать программу с базой учащихся группы (данные хранятся в файле).
Записи по учащемуся: имя, фамилия, пол, возраст. Программа должна предусматривать
поиск по одному или нескольким полям базы. Результат выводить в удобочитаемом виде с порядковым номером записи."""

# import function to find students in list
from HomeWork_05.ex5_03 import find_stud

# open file with students info
text_file = open('students_info.txt')

# create list of students without '\n' using list generator
stud_list = [line.rstrip().split() for line in text_file]

# create a [{}] - function from homework05 works using this format: [{'name':'', 'surname':'', 'sex':'', 'age':''},{..}]
keys = ['surname', 'name', 'sex', 'age']
stud_dict = [dict(zip(keys, values)) for values in stud_list]

# cirlce to call the function all time you want
while True:
    find_stud(stud_dict)
    request = input('Do yob want to continue? Y/N')
    if request == 'N' or request == 'n':
        quit()

