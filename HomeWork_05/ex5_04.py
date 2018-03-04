"""Дана квадратная матрица А(N,N). 
Составить программу подсчета количества положительных элементов, 
расположенных выше главной диагонали."""

MATRIX = [
    [1, 3, 4, -2],
    [-2, 5, -3, 4],
    [3, 6, 8, 6],
    [4, 3, 5, 0]
]


# Change all negative numbers to '0' in list
def only_positive(lst):
    for i in lst:
        if i < 0:
            pos = lst.index(i)
            lst = lst[:pos] + [0] + lst[pos + 1:]
    return lst


step = 0
total = 0
for element in MATRIX:
    element = only_positive(element)
    total += sum(element[step + 1:])
    step += 1
    print(element)

print(total)


def test_only_pos():
    if only_positive([-1,2,3,-4]) == [0,2,3,0]:
        print('test ok')


test_only_pos()