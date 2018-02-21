# Input data
str_1 = input('Please, enter the frist sting: ')
str_2 = input('Please, enter the second string: ')

# Check if second str is substring of the first str
if str_2 in str_1:
    print('Yes, second string is substring of the first string')
else:
    print("No, second string isn't substring of the first string")