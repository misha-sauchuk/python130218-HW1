# Matrix that we should use
Matrix = [
    [3, 5, 9],
    [2, 18, 36],
    [12, 2, 5]
]

# Set the initial values
av_val = 0
summ = 0
length = 0

# Count the average values of Matrix element
for list in Matrix:
    summ += sum(list)
    length += len(list)
    print(summ, length)
else:
    av_val = summ/length

print('Average value of this matrix is {0:.2f}'.format(av_val))