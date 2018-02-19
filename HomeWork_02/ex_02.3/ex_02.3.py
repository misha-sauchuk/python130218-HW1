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
# вводим данные
num_list = []
step = 0

# создаем список из введенных чисел
while step < 3:
    num = input_data()
    num_list.append(num)
    step = step + 1

# проверяем условие задачи
if num_list[0]%2 == 0 or num_list[1]%2 == 0 or num_list[2]%2 == 0:
    answer = max(num_list)
else:
    answer = min(num_list)

print('ответ: ', answer)
