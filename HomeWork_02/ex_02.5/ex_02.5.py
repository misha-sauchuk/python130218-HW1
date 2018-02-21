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
A = input_data()
B = input_data()
C = input_data()

# проверяем условие задачи
if A >= B >= C :
    A = A * 2
    B = B * 2
    C = C * 2
else:
    A,B = B,A
print('A:', A, 'B:', B, 'C: ', C )

