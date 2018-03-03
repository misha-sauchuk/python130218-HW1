d = {}
l = [1, 2, 4, 5, 1, 4, 6, 1]
# Create dict with key-numbers and values is repeated times
for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

# Create list of key-value pairs
key_val_list = list(d.items())

# Find the number with max times of repeating
maximum = None
for i in key_val_list:
    if maximum is None:
        maximum = i
    elif maximum[1]<i[1]:
        maximum = i
print('number {} is repeated {} times'.format(maximum[0], maximum[1]))
