# List of students
list = [
    {'name': 'Ivan', 'surname': 'Borisenko', 'sex': 'male', 'age': '29'},
{'name': 'Alex', 'surname': 'Zabolockii', 'sex': 'male', 'age': '28'},
{'name': 'Nina', 'surname': 'Sauchuk', 'sex': 'female', 'age': '25'},
{'name': 'Ann', 'surname': 'Sauchuk', 'sex': 'female', 'age': '31'},
{'name': 'Nadzja', 'surname': 'Kapko', 'sex': 'female', 'age': '27'},
{'name': 'Alex', 'surname': 'Buiko', 'sex': 'male', 'age': '26'}
]

# Create a dictionary with empty values
dict_check = {'name': '', 'surname': '', 'sex': '', 'age': ''}

# Fucnction to input information to search
def search_info():
    for key in dict_check.keys():
        print('Please, enter an information about {}, or press "Enter" to skip:'.format(key.upper()))
        dict_check[key] = input()
    return dict_check

# Ask function search_info
dict_check = search_info()

# Count how many parameters we use to search the student
find_numbers = 0
for value in dict_check.values():
    if value: find_numbers += 1

# Check if there are students in our list with input information
number = 0
for dic in list:
    if dic.items() & dict_check.items() and len(dic.items() & dict_check.items())==find_numbers:
        number += 1
        print('{}. {} {}, {} years old, {}'.format(number, dic['surname'], dic['name'], dic['age'], dic['sex']))



# Print result if there no coincidence
if number == 0:
    print('There are no students with input data')



