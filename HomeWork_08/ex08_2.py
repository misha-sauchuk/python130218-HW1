"""В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную.
Вывести на экран всех учащихся, чья оценка меньше 3 баллов и посчитать средний балл по классу.
"""
# open text file with students performance
text_file = open('student performance.txt')

# create a list of students without \n element using list generator
stud_group = [line.rstrip().split() for line in text_file]
print(stud_group)
# create a list of marks in all group using list generator
mark_group = [int(stud[-1]) for stud in stud_group]

# calculate the average mark in group
aver_mark = sum(mark_group)/len(mark_group)

# create a list of students with mark less than 3
stud_mark = [rec for rec in stud_group if int(rec[-1]) < 3]

# print results
for rec in stud_mark:
    print(rec[0],rec[1],rec[2])
print('Average mark of group is {}'.format(aver_mark))
