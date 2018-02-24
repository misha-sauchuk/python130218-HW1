# Create a list of input data
numbers = []
while True:
    number = input('Enter a number, or press "Enter" to stop input: ')
    if number == '':
        break
    number = int(number)
    numbers.append(number)

# Delete every element '0' and add new element '-1'
for i in numbers:
    if i == 0:
        del numbers[numbers.index(i)]
        numbers.append(-1)
print(numbers)