# Import string to create a check_list with English alphabetic and digits
import string

# Input word, that we will check
ident = input('Enter your word: ')

# Create data to make check the word
check_string = string.ascii_letters + string.digits + '_'

# Check if our word is identifier
if ident[0].isalpha() or ident[0]=='_':
    for i in ident:
        if i not in check_string:
            print('"{}" is not identifier'.format(ident))
            break
    else:
        print('"{}" is identifier'.format(ident))
else:
    print('"{}" is not identifier'.format(ident))
