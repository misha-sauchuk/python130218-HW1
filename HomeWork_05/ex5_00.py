d = {}
l = [1, 2, 4, 5, 1, 4, 6, 1]
for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = i

#print(d[1])

for keys in d:
    print(d[keys])