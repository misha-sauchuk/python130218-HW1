"""В текстовом файле посчитать количество строк,
а также для каждой отдельной строки определить количество в ней символов и слов."""

# input the file name or open the default file
text_file = input('Please, enter the name of file: ')
if not text_file:
    text_file = 'text_file.txt'

# open file
text_file = open(text_file)
count = 0

# circle to count the numbers of lines and numbers of words in line
for line in text_file:
    count += 1
    words = line.split()
    print('There are {} words in line {}'.format(len(words), count))
else:
    text_file.close()
    print('There are {} lines in text'.format(count))