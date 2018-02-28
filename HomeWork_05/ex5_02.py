# Matrix that we should use
Matrix = [
    [3, 5, 9],
    [2, 18, 36],
    [12, 0, 5],
    [150, 585, 354]
]

# Function to input a data
def input_data():
    '''Input data and return a string'''
    input_data = input()
    return input_data

# Function to change string to float
def inp_num():
    ''' Input data return in float'''
    while True:
        try:
            inp_num = float(input_data())
            #print(inp_num)
            return (inp_num)
        except:
            print('Invalid input')
            continue

# Input data
print('Please, input p1: ')
p1 = inp_num()
print('Please, input p2: ')
p2 = inp_num()

# Count elements in the range of p1 & p2
count = 0
for list in Matrix:
    for i in list:
        if p1<=i<=p2:
            count += 1

print('There are {} elements in this Matrix in the range of ({}, {})'.format(count,p1,p2))