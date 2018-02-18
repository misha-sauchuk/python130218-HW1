first_num = input ('Please, enter first integer number: ')
#while True:
try:
    first_num = int(first_num)
    #return (first_num)
except:
    print ('Invalid input')
        break#continue #quit()
first_num = int(first_num)
second_num = input ('Please, enter second integer number: ')
try:
    second_num = int(second_num)
except:
    print ('Invalid input')
    quit()
second_num = int(second_num)
summ = first_num + second_num
print ('The sum of ', first_num, ' and', second_num, ' is ', summ)
