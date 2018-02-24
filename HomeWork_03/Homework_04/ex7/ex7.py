# Fuction to input data
def input_data():
    '''Input data and return a string'''
    input_data = input()
    return input_data

# Input string and symbol
print('Please, enter a text: \n')
text = input_data()
print('Please, enter a symbol, you wold like to check: ')
symbol = input_data()

# Create a new string with upper symbol
for letter in text:
    if letter == symbol:
        new_text = text.replace(letter, letter.upper())

# Create a new string without ends
final_text = new_text[:new_text.rfind(symbol.upper())]

# Print answer
print(final_text)
