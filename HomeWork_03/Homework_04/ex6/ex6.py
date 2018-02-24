# Create a list of input data
numbers = []
while True:
    number = input('Enter a number, or press "Enter" to stop input: ')
    if number == '':
        break
    number = int(number)
    numbers.append(number)
# Create an empty lists to sort negative and positive numbers
minus = []
plus = []

# Fill the negative and positive lists
for i in numbers:
    if i < 0:
        minus.append(i)
    else:
        plus.append(i)

# Create a new list in the right position
num_list = minus + plus
print(num_list)
