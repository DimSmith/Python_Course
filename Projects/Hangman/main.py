import random

stages = ['''
  +---+
  |   |
  O   |
 (|)  |
 ( )  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 (|)  |
 (    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 (|)  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 (|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

world_list = ['camel', 'apple', 'phone', 'shoe', 'fish', 'dog']
rand_word = random.choice(world_list)
word_len = len(rand_word)

print(f"{rand_word},{word_len}")

placeholder = ""
for position in range(word_len):
    placeholder += "_"

game_over = False
correct_letters = []
lives = 6

while not game_over:
    guess_letter = input("Guess a latter:").lower()

    display = ""

    for letter in rand_word:
        if letter == guess_letter:
            display += letter
            correct_letters.append(guess_letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess_letter not in rand_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lose!")

    if "_" not in display:
        game_over = True
        print("You Win!")

    print(stages[lives])