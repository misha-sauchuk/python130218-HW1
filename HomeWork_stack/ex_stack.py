# initial data
lst = []
count = 0


# function to add number to the stack
def push(l):
    number = int(input('Please, enter a number, you would like to add:\n'))
    print('ok')
    l = l + [number]
    return l


# function to delete last number in stack and print it
def pop(l):
    print(l[-1])
    l = l[:-1]
    return l


# function to print last number in stack
def back(l):
    print(l[-1])


# function to print a length of the stack
def size():
    print(count)


# function to delete all elements from stack
def clear(l):
    print('ok')
    l = []
    return l


# function to exit the programm
def exit():
    print('bye')
    quit()


# circle to take command from users
while True:
    command = input('Please, enter your command:\n')
    if command == 'push':
        lst = push(lst)
        count += 1
        # print(lst)
    elif command == 'pop':
        lst = pop(lst)
        count -= 1
    elif command == 'back':
        back(lst)
    elif command == 'size':
        size()
    elif command == 'clear':
        lst = clear(lst)
        count = 0
    elif command == 'exit':
        exit()


# functional test to function "pop" and "clear"
def test_pop():
    if pop([1, 2, 3]) == [1, 2]:
        print('test "pop" ok')


def test_clear():
    if clear() == []:
        print('test "clear" ok')


test_pop()
test_clear()
