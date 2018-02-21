# Create list from string with upper words
str_ex = 'Hello!Anthony!Have!A!Good!Day!'
list = str_ex.upper().split('!')

# Check, if last element is empty in list
if list[-1] == '':
    list = list[:-1]

# Output answer
print(list)
