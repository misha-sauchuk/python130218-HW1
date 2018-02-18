while True:
    first_operand = input ('Please, enter first number: ')
    try:
        first_operand = float(first_operand)
    except:
        print ('Invalid input')
        break
    first_operand = float(first_operand)
    second_operand = input ('Please, enter second number: ')
    try:
        second_operand = float(second_operand)
    except:
        print ('Invalid input')
        break5
    second_operand = float(second_operand)
    operator = input ('Please, enter operator: ')
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
    print (result)
    question_continue = input ('If you want to stop please enter "N" or press Enter to continue: ')
    if question_continue == "N":
       break


