# Hangman Game
import random

name = input("Enter your name: ")
print(f"Welcome {name}")
print("-----------------------------")
print("Try to guess the words in less than 10 attempts.")


def hangman():
    word = random.choice(["Kevin", "Jim", "Michael", "Pam", "Andy", "Karen"])
    attempt = 10
    valid_letters = 'abcdefghijklmnopqrstuvwxyz'
    guess_made = ''

    while len(word) > 0:            # 1.Check if random word is valid or not
        main = ''
        for letters in word:
            if letters in guess_made:
                main += letters
            else:
                main = main + '_' + ' '

        if main == word:
            print(main)
            print("You won!")
            break

        print("Guess the word:", main)
        guess = input()

        if guess in valid_letters or valid_letters.upper():
            while guess in guess_made:
                print("Please guess another letter!")
                guess = input()
            guess_made += guess
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in word:
            attempt = attempt - 1
            if attempt == 9:
                print("You have 9 turns left")
                print("-----\n")
            if attempt == 8:
                print("You have 8 turns left")
                print("-----\n"
                      "  o  \n")
            if attempt == 7:
                print("You have 7 turns left")
                print("-----\n"
                      "  o\n"
                      "  |\n")
            if attempt == 6:
                print("You have 6 turns left")
                print("-------\n"
                      "   o\n"
                      "   |\n"
                      "  /\n")
            if attempt == 5:
                print("You have 5 turns left")
                print("-------\n"
                      "   o\n"
                      "   |\n"
                      "  / \\ \n")
            if attempt == 4:
                print("You have 4 turns left")
                print("-------\n"
                      " \ o\n"
                      "   |\n"
                      "  / \\\n")
            if attempt == 3:
                print("You have 3 turns left")
                print("--------\n"
                      " \ o /\n"
                      "   |\n"
                      "  / \\\n")
            if attempt == 2:
                print("You have 2 turns left")
                print("--------\n"
                      " \ o /|\n"
                      "   |\n"
                      "  / \\\n")
            if attempt == 1:
                print("You have 1 turns left")
                print("--------\n"
                      " \ o /_|\n"
                      "   |\n"
                      "  / \\\n")
            if attempt == 0:
                print("You have 0 turns left")
                print("you lose")
                print("------\n"
                      "   o_|\n"
                      "  /|\\\n"
                      "  / \\\n")
                break


hangman()
print()
