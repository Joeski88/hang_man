import os, random, string
from words import words
from colorama import init, Fore, Back, Style
from time import sleep

init(autoreset=True)

from player import Player

global players
players = []

punct = string.punctuation
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
            main()
        
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
                #player.update_to_initial_state(self)
                break

            ### win state
            if current_player.current_letters_right >= current_player.length_of_word_to_guess:
                print(Fore.YELLOW + Back.GREEN + " YOU WONNN!")
                #player.update_to_initial_state(self)
                main()
                break

            if len(current_player.current_letters_guessed) >= 1:
                print(Fore.YELLOW + "\n Letters guessed so far:\n ")

            for letter in current_player.current_letters_guessed:
                print(Fore.RED + letter, end="  ")

                # prompt for user input
            letterGuessed = input("\n Guess a letter (attempts left=%d): \n" %(tries - current_player.amount_of_times_wrong))
                
            isValid = checkValid(letterGuessed)

            if not isValid or letterGuessed == " ": 
                print(Fore.GREEN + "Valid characters are A-Z & a-z, No special characters allowed")
                run()

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

def main():
    players = [] # reset global player array after each new game. 
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
        print(Fore.YELLOW + Back.BLUE + " 3) Exit Game")

        choice = input(Fore.GREEN + " Menu Select: \n")
        choice = choice.strip()
        if (choice == "1"):
            print("Let's Playyyyyyy!!!")
            print("Enter number of players: (1-3 max)")
                    
            player_num = input()                
            player_num = int(player_num)
            
            print("Number of players:", player_num)
            for p in range(player_num):
                print("Enter player name:")
                name = input()
                player = addPlayer(name)
                randomWord = getWord()
                player.setWord(randomWord)
                
            run() #THIS WAS INDENTED.

        elif (choice == "2"):
                    print(Fore.CYAN + "\n1. A word is generated at random.\n2. Select desired letters. \n3. Keep guessing letters until you either guess the word or the hangman hangs!!!\n  \n------------------------------------------------------")
        elif(choice == "3"):
                    print(Fore.GREEN + " Thank you for playing!!!")
                    break                
        else:
                print(Fore.RED + " Invalid Choice, Please Try Again.")


if __name__ == "__main__": 
    main()
