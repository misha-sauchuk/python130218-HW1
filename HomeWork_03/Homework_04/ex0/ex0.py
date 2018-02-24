# Create list with user's numbers
numbers = []
while True:
    number = input('Enter a number, or press "Enter" to stop input: ')
    if number == '':
        break
    number = int(number)
    numbers.append(number)

# Count, How many times user's number is appear in the list
a = int(input('Enter number:'))
count = 0
for i in numbers:
    if i == a:
        count = count + 1

# Print answer
print('count {}'.format(count))




