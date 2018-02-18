#функция ввода данных и проверки ввода
def input_data():
    while True:
        input_data = input('Please, enter a number: ')
        try:
            input_data = int(input_data)
            return input_data
        except:
            print('Invalid input')
            continue

#цикл проверки четности числа
while True:
    number = input_data()
    result = number%2
    if result == 0:
        print('Your number is even')
    else:
        print('Your number is odd')
    to_stop = input('To stop please enter "S" or press enter to continue: ')
    to_stop = to_stop.capitalize()
    if to_stop =="S":
        break
