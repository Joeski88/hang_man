import random
from words import words

# testflag for debugging
TESTFLAG = False

def testWord(randomWord, TESTFLAG):
    if TESTFLAG == True:
        print("WORD TO GUESS", randomWord)

def testWrongGuess(total, TESTFLAG):
    if TESTFLAG == True:        
        print("Amountoftimewrong", total)

def print_hangman(wrong):
    if(wrong == 1):
        print("\n+=====+")
    elif(wrong == 2):
        print("\n+====+")
        print("       |")
        print("       |")
        print("       |")
    elif(wrong == 3):
        print("\n+====+")
        print("       |")
        print("       |")
        print("       |")
        print("  ======")
    elif(wrong == 4):
        print("\n+====+")
        print("  O    |")
        print("       |")
        print("       |")
        print("  ======")
    elif(wrong == 5):
        print("\n+====+")
        print("  O    |")
        print("  |    |")
        print("       |")
        print("  ======")
    elif(wrong == 6):
        print("\n+====+")
        print("  O    |")
        print(" /|    |")
        print("       |")
        print("  ======")
    elif(wrong == 7):
        print("\n+====+")
        print("  O    |")
        print(" /|\   |")
        print("       |")
        print("  ======")
    elif(wrong == 8):
        print("\n+====+")
        print("  O    |")
        print(" /|\   |")
        print(" /     |")
        print("  ======")
    elif(wrong == 9):
        print("\n+====+")
        print("  O    |")
        print(" /|\   |")
        print(" / \   |")
        print("  ======")

def printWord(randomWord, guessedLetters):
    counter=0
    rightLetters=0
    for char in randomWord:
        if(char in guessedLetters):
            print(randomWord[counter], end=' ')
            rightLetters += 1 # ADDED - to fix main bug, it wasn't being updated so was always 0
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

    for x in randomWord:
        print("_", end=" ")

    while(True):
        ## ADDED
        if amount_of_times_wrong >= 9:
            print("\nGAME OVER!")
            break
        print("\nLetters guessed so far:\n ")
        for letter in current_letters_guessed:
            print(letter, end=" ")
        ### ADDED
        if current_letters_right >= length_of_word_to_guess:
            print("\nYOU WONNN!")
            break

        ### prompt for user input
        letterGuessed = input("\nGuess a letter: \n")

        ### User is right
        for current_guess_index in range(length_of_word_to_guess):
            if randomWord[current_guess_index] == letterGuessed:
                current_letters_guessed.append(letterGuessed)

                current_letters_right = printWord(randomWord, current_letters_guessed)
                #print("Right", (randomWord[current_guess_index], current_guess_index, [current_letters_right]), length_of_word_to_guess, current_letters_right >= length_of_word_to_guess)
                break            

        ### User wrong
        if (randomWord[current_guess_index] != letterGuessed):

            if(current_letters_right < length_of_word_to_guess):
                amount_of_times_wrong += 1

                current_letters_guessed.append(letterGuessed)

                ### Update drawing
                print_hangman(amount_of_times_wrong)

                ### Print word
                current_letters_right = printWord(randomWord, current_letters_guessed)
                testWrongGuess(amount_of_times_wrong, TESTFLAG)

        printLines(randomWord)

        #print([amount_of_times_wrong], current_letters_right, randomWord, (current_guess_index), letterGuessed, randomWord[current_guess_index] == letterGuessed)

### Welcome message
    def main():
        print(f"""
--------------------------------------------------------------------------------
            _   _    _    _   _  ____ __  __    _    _   _ _ 
            | | | |  / \  | \ | |/ ___|  \/  |  / \  | \ | | |
            | |_| | / _ \ |  \| | |  _| |\/| | / _ \ |  \| | |
            |  _  |/ ___ \| |\  | |_| | |  | |/ ___ \| |\  |_|
            |_| |_/_/   \_\_| \_|\____|_|  |_/_/   \_\_| \_(_)

--------------------------------------------------------------------------------
    """)

### Start menu for user
choice = ""

while True:
        print("\n1) Play Game")
        print("2) Rules")
        print("3) Language Select Mode")
        print("4) Multiplayer")
        print("5) Exit Game\n")

        choice = input("Menu Select: \n")

        choice = choice.strip()
        if (choice == "1"):
                print("\nLet's Playyyyyyy!!!\n")
                run()
        elif (choice == "2"):
                print("\n1. A word is generated at random.\n2. Select desired letters. \n3. Keep guessing letters until you either guess the word or the hangman hangs!!!\n  \n------------------------------------------------------")
        elif(choice == "5"):
                break
        else:
            print("Invalid Choice, Please Try Again.")


if __name__ == "__main__": 
    main()
