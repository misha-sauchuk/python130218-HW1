# Import string to create a check_list with English alphabetic and digits
import string

# Input word, that we will check
ident = input('Enter your word: ')

# Create data to make check the word
check = 0
check_string = string.ascii_letters + string.digits + '_'

# Look through the input word to find needfull elements
for i in ident:
    if i in check_string:
        check = check + 1

# Check if word is identifier
if check == len(ident):
    print('"{}" is identifier'.format(ident))
else:
    print('"{}" is not identifier'.format(ident))