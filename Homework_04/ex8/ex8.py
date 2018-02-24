# initial list of grades
grades = [('Ann', 9), ('John', 7), ('Smith', 5), ('George', 6)]

# create an empty lists of reverse grades like "[9, 'Ann']"
grades_reverse = []
for element in grades:
    grades_reverse.append([element[1],element[0]])

# create an empy list where we will put elements in order for max mark to min mark
gades_mark = []
while len(grades_reverse) > 0:
    gades_mark.append(grades_reverse.pop(grades_reverse.index(max(grades_reverse))))
    #print(new_grades)

# print answer
for element in gades_mark:
    print('Hello {}! your grade is {}'.format(element[1], element[0]))

