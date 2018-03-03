# Input text and create a list with separated words
text = input('Please, enter your text: \n')
list_text = text.split(' ')

# Create a string with all vowels of English and Russian alpabets
check_str = 'AEIOYUeyuioaУЕЁЫАОЭЯИЮёуеаоэяиюы'

# Find the position of the shortest word in the list
position = None
min_len = None
for word in list_text:
    if min_len is None:
        min_len = len(word)
        position = list_text.index(word)
    elif len(word) < min_len:
        min_len = len(word)
        position = list_text.index(word)

# Find all vowels in the shortest word using the data stucture 'set'
vowels = set()
shortest_word = list_text[position]
for letter in shortest_word:
    if letter in check_str:
        vowels.add(letter)


print('All vowels in the sortest word is: {}'.format(vowels))
