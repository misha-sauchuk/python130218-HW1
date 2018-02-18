import math
diameter = input ('Please, enter diameter of circle: ')
try:
    diameter = float(diameter)
except:
    print ('Invalid input')
    quit()
diameter = float(diameter)
square_circle = math.pi * diameter / 4
print ('The square of circle is: ', square_circle)
question_modify = input ('Do you want to modify the answer: Y/N?')
if question_modify == 'Y':
    round_num = input ('Please, enter how you wolud like to round the answer: ')
    round_num = int(round_num)
    square_circle_mod = round(square_circle, round_num)
    print ('The modify answer is: ', square_circle_mod)
    

