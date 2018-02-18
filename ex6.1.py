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

# калькулятор
while True:
    first_operand = input_data()
    second_operand = input_data()
    operator = input('Please, enter operator: ')
    if operator == '+':
        result = first_operand + second_operand
    elif operator == '-':
        result = first_operand - second_operand
    elif operator == '*':
        result = first_operand * second_operand
    elif operator == '/':
        result = first_operand / second_operand
    else:
        result = 'NaN'
    print(result)
    question_continue = input('If you want to stop please enter "N" or press Enter to continue: ')
    question_continue = question_continue.capitalize()
    if question_continue == "N":
        break
