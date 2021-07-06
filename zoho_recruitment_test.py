word = input()
word_length = len(word)
middle = word_length//2
formatted_word = ''
for i in range(word_length):
    formatted_word += word[middle]
    print(' '*(word_length-i-1)+formatted_word)
    middle += 1
    if middle == word_length:
        middle = 0