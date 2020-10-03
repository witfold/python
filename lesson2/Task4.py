words = list(input('Put some words with spacing: ').split(' '))

for index, word in enumerate(words, 1):
    print(f'{index} {word if len(word) < 10 else word[0:10]}')
