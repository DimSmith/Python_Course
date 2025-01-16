import random

world_list = ['camel', 'apple', 'phone', 'shoe', 'fish', 'dog']
rand_word = random.choice(world_list)
word_len = len(rand_word)

print(f"{rand_word},{word_len}")

placeholder = ""
for position in range(word_len):
    placeholder += "_"

game_over = False

while not game_over:
    guess_letter = input("Guess a latter:").lower()

    display = ""

    for letter in rand_word:
        if letter == guess_letter:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You win.")
