import random
from word_list import word_list
from art import stages
from art import logo

rand_word = random.choice(word_list)
word_len = len(rand_word)

print(f"{rand_word},{word_len}")

placeholder = ""
for position in range(word_len):
    placeholder += "_"

game_over = False
correct_letters = []
lives = 6

print(logo)

while not game_over:
    print(f"*****************{lives}/6 LIVES LEFT*****************")
    guess_letter = input("Guess a latter:").lower()
    if guess_letter in correct_letters:
        print("You have already guess this letter")
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
        print(f"You guessed {guess_letter}, that's not in the word. You lose a life")
        if lives == 0:
            game_over = True
            print(f"*****************IT WAS {rand_word}! YOU LOSE*****************")

    if "_" not in display:
        game_over = True
        print("*****************YOU WIN*****************")

    print(stages[lives])
