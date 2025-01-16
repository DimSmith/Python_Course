import random

world_list = ['camel', 'apple', 'phone', 'shoe', 'fish', 'dog']
rand_word = random.choice(world_list)
word_len = len(rand_word)

print(f"{rand_word},{word_len}")

placeholder = ""
for position in range(word_len):
    placeholder += "_"


display = ""
guess_letter = input("Guess a latter:").lower()

for letter in rand_word:
    if letter == guess_letter:
        display += letter
    else:
        display += "_"

print(display)