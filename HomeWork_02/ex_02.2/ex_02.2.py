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

# вводим данные для уравнения
print('Please, enter expression arguments: "A", "D" and "C", ')
A = input_data()
D = input_data()
C = input_data()

# вводим корни х и у, которые будем проверять
print('Please, enter "X" and "Y", you would like to check')
x = input_data()
y = input_data()

# проврека корней на решение уравнения
if (A*x**4+D*x**2+C) == 0 and (A*y**4+D*y**2+C) == 0:
    print('x and y is correct')
else:
    print ('x and y is incorrect')