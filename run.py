import os, random, string
from words import words
from colorama import init, Fore, Back, Style
from time import sleep

init(autoreset=True)

from player import Player

global players
players = []

####################################
punct = string.punctuation + " " # Capture whitespace.
####################################

numbers = "0123456789"
tries = 9

invalid_chars = punct + numbers

# testflag for debugging
TESTFLAG = False

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

# function for adding player name
def addPlayer(name):
    p = Player(name)
    players.append(p)
    return p

# debugging testflag
def testWord(randomWord, TESTFLAG):
    if TESTFLAG == True:
        print("WORD TO GUESS", randomWord)

def testWrongGuess(total, TESTFLAG):
    if TESTFLAG == True:
        print("Amountoftimeswrong", total)

# function for checking invalid characters
def checkValid(char):
    if char in invalid_chars:
        return False
    else:
        return True


""" Hangman terminal visuals """

def print_hangman(wrong):
    if(wrong == 1):
        print("+=====+")
    elif(wrong == 2):
        print(f"""\n
                   +====+
                        |
                        |
                        |""")
    elif(wrong == 3):
        print(f"""\n
                   +====+
                        |
                        |
                        |
                    ======= """)
    elif(wrong == 4):
        print(f"""\n
                   +====+
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
                   /|\\  |
                        |
                    ======= """)
    elif(wrong == 8):
        print(f"""\n+====+
                    O   |
                   /|\\  |
                   /    |
                    ======= """)
    elif(wrong == 9):
        print(f"""\n+====+
                    O   |
                   /|\\  |
                   / \\  |
                    ======= """)


""" main game loop and counter """


# counter
def printWord(randomWord, guessedLetters):
    rightLetters=0
    displayWord= ""
    # loop to print correct letters in word
    for char in randomWord:
        if char in guessedLetters:
            displayWord += char + ' '
            rightLetters += 1
        else:
            displayWord += '_ '
    print(displayWord.strip())
    return rightLetters

def getWord():
    # pick a random word from list
    randomWord = random.choice(words)
    # testflag for debugging. change to true at the top of the page to use
    testWord(randomWord, TESTFLAG)
    return randomWord
    
    
    # Runs the game
def run():
    while(True):
        if len(players) == 0:
            mainMenu()
        
        for p in range(len(players)):

            current_player = players[p]
            
            print("\nYour turn %s!\n" %(current_player.name))
            printWord(current_player.randomWord, current_player.current_letters_guessed)
            

            # Game over state
            if current_player.amount_of_times_wrong >= tries:
                current_player.GAME_OVER = True
                print(Fore.BLACK + Back.RED + " GAME OVER! %s :( "%(current_player.name))
                print(Fore.BLACK + Back.RED + " Your word was...")
                print(Fore.YELLOW + current_player.randomWord)
                
                players.pop(p)
                break

            ### win state
            if current_player.current_letters_right >= current_player.length_of_word_to_guess:
                print(Fore.YELLOW + Back.GREEN + " YOU WONNN!")
                ####################################
                mainMenu() # Call main menu
                ####################################
                break

            if len(current_player.current_letters_guessed) >= 1:
                print(Fore.YELLOW + "\n Letters guessed so far:\n ")

            for letter in current_player.current_letters_guessed:
                print(Fore.RED + letter, end="  ")

            # prompt for user input
            letterGuessed = input("\n Guess a letter (attempts left=%d): \n" %(tries - current_player.amount_of_times_wrong))
                
            isValid = checkValid(letterGuessed)

            if not isValid or letterGuessed == "": 
                print(Fore.GREEN + "Valid characters are A-Z & a-z, No special characters allowed")
                run()

            #### Check if already guessed ######
            if letterGuessed in current_player.current_letters_guessed:
                print("You already guessed '%s'" %(letterGuessed))
                run()
            ####################################
                
            # User is right
            for current_player.current_guess_index in range(current_player.length_of_word_to_guess):
                if current_player.randomWord[current_player.current_guess_index] == letterGuessed:
                    current_player.current_letters_guessed.append(letterGuessed)
                    current_player.current_letters_right = printWord(current_player.randomWord, current_player.current_letters_guessed)
                    break
            # User wrong
            if (current_player.randomWord[current_player.current_guess_index] != letterGuessed):
                if(current_player.current_letters_right < current_player.length_of_word_to_guess):
                    current_player.amount_of_times_wrong += 1
                    current_player.current_letters_guessed.append(letterGuessed)
                    # Update drawing
                    print_hangman(current_player.amount_of_times_wrong)
                    # Print word
                    current_player.current_letters_right = printWord(current_player.randomWord, current_player.current_letters_guessed)
                    testWrongGuess(current_player.amount_of_times_wrong, TESTFLAG)

""" Main game menu loop """
###### Added new function to get number of players

def getNumberOfPlayers():
    print("Enter number of players: (1-3 max)")
    player_num = input()

    ##### Added validation checks on number of players
    if player_num in punct or player_num == "":
        print("Not a valid number! Please try again.")
        getNumberOfPlayers()
    ####################################
        
    player_num = int(player_num)

    ##### Check number is in range of 1 to 3 and not less than 0
    if player_num <= 0:
        print(Fore.RED + "The min number of players is 1! Try again.")
        getNumberOfPlayers()
    ##### Check number is in range of 1 to 3 and not greater than 3
    elif player_num > 3:
        print(Fore.RED + "The max number of players is 3! Try again.")
        getNumberOfPlayers()
    ##############################################
    else:        
        print(Fore.GREEN + "Number of players:", player_num)
        for p in range(player_num):
            print(Fore.GREEN + "Enter player name:")
            name = input()

            #### Remove white space from name on the left and right
            name = name.lstrip().rstrip()
            if name == "":
                mainMenu()
            ##############################
            player = addPlayer(name)
            randomWord = getWord()
            player.setWord(randomWord)

        #### Corrected bug in multiplayer option 
        print(Fore.GREEN + "Let's Playyyyyyy!!!")
        
        run() #THIS WAS INDENTED.
        ########################################

#### Refactored main() to mainMenu()
def mainMenu():
    players = [] # reset global player array after each new game. 
    # Start menu for user
    choice = ""
   
    print(Fore.WHITE + """
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
        print(Fore.YELLOW + Back.BLUE + " 3) Exit Game")

        choice = input(Fore.GREEN + " Menu Select: \n")
        choice = choice.strip()
        
        #### Added validation to check enter key without valid input
        if choice == "":
            mainMenu()
            
        if (choice == "1"):
            #### refactored into a function
            getNumberOfPlayers()
            ###############################

        elif (choice == "2"):
               print(Fore.CYAN + "\n1. A word is generated at random.\n2. Select desired letters. \n3. Keep guessing letters until you either guess the word or the hangman hangs!!!\n  \n------------------------------------------------------")
        elif(choice == "3"):
               print(Fore.GREEN + " Thank you for playing!!!")
               break                
        else:
               print(Fore.RED + " Invalid Choice, Please Try Again.")


if __name__ == "__main__":
    #### Refactored main() to mainMenu()
    mainMenu()
