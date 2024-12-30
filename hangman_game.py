import random
import os
import hangman_stages
import word_file

lives = 6
chosen_word = random.choice(word_file.words)
print(f"Debug: The chosen word is {chosen_word}")

display = ['_' for _ in chosen_word]
game_over = False

while not game_over:
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Hangman Game")
    print(hangman_stages.stages[lives])
    print(f"Word: {' '.join(display)}")
    print(f"Lives remaining: {lives}")

    guessed_letter = input("Guess a Letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter

    if guessed_letter not in chosen_word:
        lives -= 1
        print(f"Wrong guess! Lives remaining: {lives}")
        if lives == 0:
            game_over = True
            os.system('cls' if os.name == 'nt' else 'clear')
            print(hangman_stages.stages[0])
            print("You Lose !!")
            print(f"The word was: {chosen_word}")
            break

    if '_' not in display:
        game_over = True
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Congratulations! You win!!")
        print(f"The word is: {''.join(display)}")
        break
