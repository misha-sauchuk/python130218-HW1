# Check correct input data
def input_data():
    while True:
        input_data = input('Enter invitation: "Dear...').upper() # upper method used to make 'mr'avalible to use
        if input_data == 'MR' or input_data == 'MRS' or input_data == 'MISS' or input_data == 'MS':
            return input_data
        else:
            print('Invalid input')
            continue

# Create a list with one element
invitation = [input_data()]

# Chekc the correct sex
if 'MR' in invitation:
    print('The sex is male')
else:
    print('The sex is female')
