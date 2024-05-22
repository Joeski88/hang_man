import random, string
from words import words
from colorama import init, Fore, Back, Style
init(autoreset=True)

punct = string.punctuation
numbers = "0123456789"

invalid_chars = punct + numbers

# testflag for debugging
TESTFLAG = False


def testWord(randomWord, TESTFLAG):
    if TESTFLAG == True:
        print("WORD TO GUESS", randomWord)


def testWrongGuess(total, TESTFLAG):
    if TESTFLAG == True:
        print("Amountoftimeswrong", total)


def checkValid(char):
    if char in invalid_chars:
        return False
    else:
        return True


"""
Hangman terminal visuals
"""


def print_hangman(wrong):
 if(wrong == 1):
    print(f"""\n+=====+""")
    elif(wrong == 2):
        print(f"""\n+====+
                        |
                        |
                        |""")
    elif(wrong == 3):
        print(f"""\n+====+
                        |
                        |
                        |
                    ======= """)
    elif(wrong == 4):
        print(f"""\n+====+
                    O   |
                        |
                        |
                    ======= """)
    elif(wrong == 5):
        print(f"""\n+====+
                    O   |
                    |   |
                        |
                    ======= """)
    elif(wrong == 6):
        print(f"""\n+====+
                    O   |
                   /|   |
                        |
                    ======= """)
    elif(wrong == 7):
        print(f"""\n+====+
                    O   |
                   /|\  |
                        |
                    ======= """)
    elif(wrong == 8):
        print(f"""\n+====+
                    O   |
                   /|\  |
                   /    |
                    ======= """)
    elif(wrong == 9):
        print(f"""\n+====+
                    O   |
                   /|\  |
                   / \  |
                    ======= """)


"""
main game loop and counter
"""


# counter
def printWord(randomWord, guessedLetters):
 counter=0


rightLetters=0
    for char in randomWord:
        if(char in guessedLetters):
            print(randomWord[counter], end=' ')
            rightLetters += 1  # ADDED-to fix main bug, it wasn't being updated
        else:
            print(" ", end=" ")
        counter += 1
    return rightLetters


def printLines(randomWord):
    print("\r")
    for char in randomWord:
        print("\u203E", end=" ")


def getWord():
    # pick a random word from list
    randomWord = random.choice(words)
    # testflag for debugging. change to true at the top of the page to use
    testWord(randomWord, TESTFLAG)
    return randomWord
    # Runs the game


def run():
    randomWord = getWord()
    length_of_word_to_guess = len(randomWord)

    current_guess_index = 0
    current_letters_guessed = []
    current_letters_right = 0

    amount_of_times_wrong = 0
# prints underscores instead of the letters of random word
    for x in randomWord:
        print(Fore.RED + Back.WHITE + " _", end=" ")

    # while loop for all possible game endings
    while(True):
        # ADDED
        if amount_of_times_wrong >= 9:
            print(Fore.RED + "\n GAME OVER! :( ")
            print(Fore.RED + "\n Your word was...")
            print(Fore.YELLOW + randomWord)
            break
        if len(current_letters_guessed) >= 1:
            print(Fore.YELLOW + "\n Letters guessed so far:\n ")
        for letter in current_letters_guessed:
            print(Fore.RED + letter, end="  ")
        # ADDED
        if current_letters_right >= length_of_word_to_guess:
            print(Fore.CYAN + "\n YOU WONNN!")
            break

        # prompt for user input
        letterGuessed = input("\n Guess a letter: \n")  # BUGHERE color issue.

        isValid = checkValid(letterGuessed)
        if not isValid: 
            print(Fore.GREEN + "Valid characters are A-Z & a-z")
            run()

        # User is right
        for current_guess_index in range(length_of_word_to_guess):
            if randomWord[current_guess_index] == letterGuessed:
                current_letters_guessed.append(letterGuessed)

                current_letters_right = printWord(randomWord, current_letters_guessed)
                # print("Right", (randomWord[current_guess_index], current_guess_index, [current_letters_right]), length_of_word_to_guess, current_letters_right >= length_of_word_to_guess)
                break            

        # User wrong
        if (randomWord[current_guess_index] != letterGuessed):

            if(current_letters_right < length_of_word_to_guess):
                amount_of_times_wrong += 1

                current_letters_guessed.append(letterGuessed)

                # Update drawing
                print_hangman(amount_of_times_wrong)

                # Print word
                current_letters_right = printWord(randomWord, current_letters_guessed)
                testWrongGuess(amount_of_times_wrong, TESTFLAG)

        printLines(randomWord)

        #print([amount_of_times_wrong], current_letters_right, randomWord, (current_guess_index), letterGuessed, randomWord[current_guess_index] == letterGuessed)

# Welcome message
    def main():

        print(f"""
-------------------------------------------------------------------------------\n
             _   _    _    _   _  ____ __  __    _    _   _ _ \n
            | | | |  / \  | \ | |/ ___|  \/  |  / \  | \ | | |\n
            | |_| | / _ \ |  \| | |  _| |\/| | / _ \ |  \| | |\n
            |  _  |/ ___ \| |\  | |_| | |  | |/ ___ \| |\  |_|\n
            |_| |_/_/   \_\_| \_|\____|_|  |_/_/   \_\_| \_(_)\n

--------------------------------------------------------------------------------\n
""")


# Start menu for user
choice = ""


while True:
    print(Fore.GREEN + "\n 1) Play Game")
    print(Fore.YELLOW + " 2) Rules")
    print(Fore.RED + " 3) Language Select Mode")
    print(Fore.CYAN + " 4) Multiplayer")
    print(Fore.BLUE + " 5) Exit Game\n")

    choice = input(Fore.GREEN + " Menu Select: \n")
    choice = choice.strip()
    if (choice == "1"):
                print(Fore.YELLOW + Back.RED + "\n  Let's Playyyyyyy!!!\n")
                run()

    elif (choice == "2"):
                print(Fore.CYAN + "\n1. A word is generated at random.\n2. Select desired letters. \n3. Keep guessing letters until you either guess the word or the hangman hangs!!!\n  \n------------------------------------------------------")
        elif(choice == "5"):
                print(Fore.GREEN + " Thank you for playing!!!")
                break                
        else:
            print(Fore.RED + " Invalid Choice, Please Try Again.")


if __name__ == "__main__": 
    main()
