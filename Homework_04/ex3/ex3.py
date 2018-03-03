# Function to input elements and create a list
def inp_lst():
    inp_lst = []
    while True:
        inplst = input('Enter an element to list, or press "Enter" to stop input: ')
        if inplst == '':
            break
        inp_lst.append(inplst)
    return inp_lst

# Request about quantity of lists
numbers_of_lists = int(input('Enter how many lists you wolud like to check: '))
x = 0
exersice_list = []
while x < numbers_of_lists:
    exersice_list.append(x)
    x += 1
print(exersice_list)

# Creating a lists using fuction 'inp_list'
for i in exersice_list:
    exersice_list[i] = inp_lst()
print(exersice_list)

# Find the length of the largest list in all amount of lists
max_len = None
for element in exersice_list:
    if max_len is None:
        max_len = len(element)
    elif len(element) >= max_len:
        max_len = len(element)

# Find all largest lists in all amount of lists
largest_lists = []
for element in exersice_list:
    if len(element) == max_len:
        largest_lists.append(exersice_list.index(element))


print(largest_lists)
#print(exersice_list[position])




