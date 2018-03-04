"""Для решений задач занятия №5 вынести общие части в модули.
Сделать единую точку входа app.py. Необходимо реализовать возможность старта
выполнения кода одного из заданий сразу после запуска программы,
а также после его выполнения предоставить возможность выполнить другое задание
без повторного запуска программы."""

# Run the first exercise in HomeWork_05
import HomeWork_05.ex5_00


# Function to ask user what to do: to continue running code or to stop
def ask_to_continue():
    ask = input('\n\tDo you want to continue running exercises?\n '
                    '\tinput "yes" to continue or press "Enter" to quit ')
    return ask


# Function to import exercise from HomeWork_05. Use can choose exercise
def running_ex():
    ex = input('\nPlease, enter number (1, 2, 3 or 4) of exercise you would like to run: ')
    if ex == '1':
        from HomeWork_05 import ex5_01
    elif ex == '2':
        from HomeWork_05 import ex5_02
    elif ex == '3':
        from HomeWork_05 import ex5_03
    elif ex == '4':
        from HomeWork_05 import ex5_04


# Circle to run code until user stop
while True:
    to_continue = ask_to_continue()
    if to_continue:
        running_ex()
    else:
        quit()


