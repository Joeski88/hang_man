import random, string
from words import words
from colorama import init, Fore, Back, Style
init(autoreset=True)

from player import Player

players = []

punct = string.punctuation
numbers = "0123456789"

invalid_chars = punct + numbers

# testflag for debugging
TESTFLAG = False


def addPlayer(name):
    p = Player(name)
    players.append(p)
    return p

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
        print("\n+=====+")
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
                   /|\\ |
                        |
                    ======= """)
    elif(wrong == 8):
        print(f"""\n+====+
                    O   |
                   /|\\ |
                   /    |
                    ======= """)
    elif(wrong == 9):
        print(f"""\n+====+
                    O   |
                   /|\\ |
                   / \\ |
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
    while(True):
        for player in players:
            print("\nYour turn %s!\n" %(player.name))
            #printLines(player.randomWord)
            for x in player.randomWord:
                # prints underscores instead of the letters of random word
                print(Fore.RED + Back.WHITE + "_", end=" ")

            # while loop for all possible game endings
            # Game over state
            if player.amount_of_times_wrong >= 9:
                print(Fore.RED + "\n GAME OVER! :( ")
                print(Fore.RED + "\n Your word was...")
                print(Fore.YELLOW + player.randomWord)
                menu()
                break

            ### win state
            if player.current_letters_right >= player.length_of_word_to_guess:
                print(Fore.CYAN + Back.GREEN + "\n YOU WONNN!")
                menu()
                break

            if len(player.current_letters_guessed) >= 1:
                print(Fore.YELLOW + "\n Letters guessed so far:\n ")

            for letter in player.current_letters_guessed:
                print(Fore.RED + letter, end="  ")

            # prompt for user input
            letterGuessed = input("\n Guess a letter: \n")
                
            isValid = checkValid(letterGuessed)

            if not isValid or letterGuessed == "": 
                print(Fore.GREEN + "Valid characters are A-Z & a-z, No special characters allowed")
                run()

            # User is right
            for player.current_guess_index in range(player.length_of_word_to_guess):
                if player.randomWord[player.current_guess_index] == letterGuessed:
                    player.current_letters_guessed.append(letterGuessed)

                    player.current_letters_right = printWord(player.randomWord, player.current_letters_guessed)
                    # print("Right", (randomWord[current_guess_index], current_guess_index, [current_letters_right]), length_of_word_to_guess, current_letters_right >= length_of_word_to_guess)          
                    break
            # User wrong
            if (player.randomWord[player.current_guess_index] != letterGuessed):

                if(player.current_letters_right < player.length_of_word_to_guess):
                    player.amount_of_times_wrong += 1

                    player.current_letters_guessed.append(letterGuessed)

                    # Update drawing
                    print_hangman(player.amount_of_times_wrong)

                    # Print word
                    player.current_letters_right = printWord(player.randomWord, player.current_letters_guessed)
                    testWrongGuess(player.amount_of_times_wrong, TESTFLAG)


        #print([amount_of_times_wrong], current_letters_right, randomWord, (current_guess_index), letterGuessed, randomWord[current_guess_index] == letterGuessed)

# Welcome message


def main():
# Start menu for user
    choice = ""

    print(f"""
--------------------------------------------------------------------------
             _   _    _    _   _  ____ __  __    _    _   _ _ 
            | | | |  / \\  | \\ | |/ ___|  \\/  |  / \\  | \\ | | |
            | |_| | / _ \\ |  \\| | |  _| |\\/| | / _ \\ |  \\| | |
            |  _  |/ ___ \\| |\\  | |_| | |  | |/ ___ \\| |\\  |_|
            |_| |_/_/   \\_\\_| \\_|\\____|_|  |_/_/   \\_\\_| \\_(_)

--------------------------------------------------------------------------""")

    while True:
        print(Fore.YELLOW + Back.MAGENTA + " 1) Play Game")
        print(Fore.YELLOW + Back.RED + " 2) Rules")
        print(Fore.YELLOW + Back.GREEN + " 3) Language Select Mode")
        #print(Fore.YELLOW + Back.CYAN +  " 4) Multiplayer")
        print(Fore.YELLOW + Back.BLUE + " 4) Exit Game")

        choice = input(Fore.GREEN + " Menu Select: \n")
        choice = choice.strip()
        if (choice == "1"):
            print("Let's Playyyyyyy!!!")
            print("Enter number of players:")
        
            player_num = input()
            player_num = int(player_num)
            for p in range(player_num):
                print("Enter player name:")
                name = input()
            
                player = addPlayer(name)
            
                randomWord = getWord()
                player.setWord(randomWord)
            
            run()

        elif (choice == "2"):
                    print(Fore.CYAN + "\n1. A word is generated at random.\n2. Select desired letters. \n3. Keep guessing letters until you either guess the word or the hangman hangs!!!\n  \n------------------------------------------------------")
        elif(choice == "4"):
                    print(Fore.GREEN + " Thank you for playing!!!")
                    break                
        else:
                print(Fore.RED + " Invalid Choice, Please Try Again.")


if __name__ == "__main__": 
    main()
