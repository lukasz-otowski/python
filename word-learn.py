import random
org_word = input('write your word, you can use big and small letters, space, ?, !, comma, and apostrophe:')
word_learn = []
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
       'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
       '?', '!', ' ', ',', '\'']

iteration = 0

# fill comparison array by random char to get the same length as original word
while iteration < len(org_word):
    rand_char = random.choice(abc)
    word_learn.insert(iteration, rand_char)
    iteration += 1

# learn the original word
while str != org_word:
    rand_char = random.choice(abc)
    randnumb = random.randrange(0, len(org_word))
    if rand_char == org_word[randnumb]:
        word_learn[randnumb] = rand_char
        str = ''.join(word_learn)
        print(str)

print('\ndone!')
print(str)
