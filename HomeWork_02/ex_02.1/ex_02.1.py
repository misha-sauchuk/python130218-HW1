# функция запроса ввода числа и провевка правильности ввода
def input_data():
    while True:
        input_data = input('Enter number: ')
        try:
            input_data = float(input_data)
            return input_data
        except:
            print('Invalid input')
            continue

# лучше это ввести в список и спомощью функции max и min найти максиамльное и минимальное число
# а можно с помощью оператора if искать мин и макс
num_list = []
step = 0

# создаем список из введенных чисел
while step < 3:
    num = input_data()
    num_list.append(num)
    step = step + 1

# ищем максимальное и минимальное и находим их сумму
maximum = max(num_list)
minimum = min(num_list)
summa = maximum + minimum
print('Сумма максимального и минимального числа равна: ', summa)