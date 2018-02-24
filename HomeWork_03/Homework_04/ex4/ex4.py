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

# Function to check if input of percents is correct
def check_condition():
    while True:
        _number = inp_num()
        if 0 < _number < 25:
            return _number
        else:
            print ('Invalid input')
            continue

# Fuction to count the month
def count_mont():
    month = 0
    deposit = initial_deposit
    while deposit < end_deposit:
        month = month + 1
        deposit = deposit + deposit * percent / 100
    return month

print('Please, enter your initial deposit: ')
initial_deposit = inp_num()
print('Please, enter percents from 0 to 25: ')
percent = check_condition()
print('Please, enter the end of the deposit: ')
end_deposit = inp_num()

month = count_mont()

print('To achive deposit in {}, you should wait {} month'.format(end_deposit,month))