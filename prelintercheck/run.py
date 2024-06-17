import os
import random
import string
from words import words
from colorama import init, Fore, Back, Style
from player import Player

# initialise colorama library
init(autoreset=True)

# Create palatte for players colours
palettes = [{
    'prompt': Fore.YELLOW,
    'win': Fore.YELLOW + Back.CYAN,
    'lose': Fore.RED + Back.BLACK,
}, {
    'prompt': Fore.GREEN,
    'win': Fore.YELLOW + Back.GREEN,
    'lose': Fore.BLACK + Back.RED,
}, {
    'prompt': Fore.BLUE,
    'win': Fore.YELLOW + Back.GREEN,
    'lose': Fore.BLACK + Back.RED,
}]

# Store whitespace and invalid characters in input prompts.
punct = string.punctuation + " " 
numbers = "0123456789"
tries = 9
# Concatenate all invalid input for game
invalid_chars = punct + numbers


# function for adding player name
def addPlayer(name):
    p = Player(name)
    players.append(p)
    return p


# function for checking invalid characters
def checkValid(char):
    if char in invalid_chars:
        return False
    else:
        return True


""" Hangman terminal visuals """


def print_hangman(wrong):
    if (wrong == 1):
        print(f"""\n
                   +=====+""")
    elif (wrong == 2):
        print(f"""\n
                   +====+
                        |
                        |
                        |""")
    elif (wrong == 3):
        print(f"""\n
                   +====+
                        |
                        |
                        |
                +=======+ """)
    elif (wrong == 4):
        print(f"""\n
                   +====+
                    O   |
                        |
                        |
                +=======+ """)
    elif (wrong == 5):
        print(f"""\n
                   +====+
                    O   |
                    |   |
                        |
                +=======+ """)
    elif (wrong == 6):
        print(f"""\n
                   +====+
                    O   |
                   /|   |
                        |
                +=======+ """)
    elif (wrong == 7):
        print(f"""\n
                   +====+
                    O   |
                   /|\\  |
                        |
                +=======+ """)
    elif (wrong == 8):
        print(f"""\n
                   +====+
                    O   |
                   /|\\  |
                   /    |
                +=======+ """)
    elif (wrong == 9):
        print(f"""\n
                   +====+
                    O   |
                   /|\\  |
                   / \\  |
                +=======+ """)


""" main game loop and counter """


# Display player word and letters guessed so far
def printWord(randomWord, guessedLetters):
    rightLetters = 0
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
    
# function to get word
def getWord():
    # pick a random word from list
    randomWord = random.choice(words)
    return randomWord
    
    
# Runs the game
def run():
    while(True):
        if len(players) == 0:
            mainMenu()
        
        for p in range(len(players)):
            # Add boundary between player goes/players
            print("\n %s %s %s " %("=" * 20," NEXT PLAYER ","=" * 20))
            # Set current player
            current_player = players[p]
            
            print(current_player.colours['prompt'] + 
                  "\n Your turn %s!" %(current_player.name))
            printWord(current_player.randomWord, current_player.current_letters_guessed)
            

            # Check for game over state
            if current_player.amount_of_times_wrong >= tries:
                current_player.GAME_OVER = True
                print(current_player.colours['lose'] + " GAME OVER! %s :( " % (current_player.name))
                print(current_player.colours['lose'] + " Your word was...")
                print(current_player.colours['prompt'] + current_player.randomWord)
                players.pop(p)
                break

            # Check for win state
            if current_player.current_letters_right >= current_player.length_of_word_to_guess:
                print(current_player.colours['win'] + " YOU WONNN!")
                players.pop(p)

                # Show player names and words if game over
                for losing_player in players:
                    print(losing_player.colours['lose'] + " %s, your word was..." % (losing_player.name))
                    print(losing_player.colours['prompt'] + losing_player.randomWord)
                
                # Call main menu
                mainMenu() 
                #break

            # Display letters guessed so far for current player
            if len(current_player.current_letters_guessed) >= 1:
                print(current_player.colours['prompt'] + "\n Letters guessed so far: ")

            for letter in current_player.current_letters_guessed:
                print(current_player.colours['prompt'] + letter, end="  ")

            # prompt for user input
            letterGuessed = input(current_player.colours['prompt'] + "\n Guess a letter (attempts left=%d): " %(tries - current_player.amount_of_times_wrong))

            # Check for valid characters   
            isValid = checkValid(letterGuessed)

            if not isValid or letterGuessed == "": 
                print(current_player.colours['prompt'] + Fore.RED + 
                      " Valid characters are A-Z & a-z, No special characters allowed")
                run()

            # Check if letter already guessed
            if letterGuessed in current_player.current_letters_guessed:
                print(current_player.colours['prompt'] + " You already guessed '%s'" % (letterGuessed))
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
            
""" Main game menu loop """
# Get number of players

def getNumberOfPlayers():
    print(Fore.GREEN + " Enter number of players: (1-3 max)")
    player_num = input()

    # Check for invalid characters
    if player_num in punct or player_num == "":
        print(Fore.RED + " Not a valid number! Please try again.")
        getNumberOfPlayers()
    # Set number of players
    player_num = int(player_num)

    # Check number is in range of 1 to 3 and not less than 0
    if player_num <= 0:
        print(Fore.RED + " The min number of players is 1! Try again.")
        getNumberOfPlayers()
    # Check number is in range of 1 to 3 and not greater than 3
    elif player_num > 3:
        print(Fore.RED + " The max number of players is 3! Try again.")
        getNumberOfPlayers()
    else:
        # Get name and word for each player        
        print(Fore.GREEN + " Number of players:" + Fore.WHITE, player_num)
        for p in range(player_num):
            print(Fore.GREEN + " Enter player name:" + Fore.WHITE)
            name = input()

            # Remove white space from name on the left and right
            name = name.lstrip().rstrip()
            # check for ent button with no input
            if name == "":
                mainMenu()
            # Initialise player
            player = addPlayer(name)
            randomWord = getWord()
            player.setWord(randomWord)
            player.setColour(palettes[p])

        # Corrected bug in multiplayer option 
        print(Fore.GREEN + " Let's Playyyyyyy!!!")
    # Run game   
    run()

# Main menu
def mainMenu():

    global players
    players = []  # reset global player array after each new game.

    GAME_RUNNING = True

    # Start menu for user
    choice = ""

    # Print main title
    print(Fore.WHITE + """
--------------------------------------------------------------------------
             _   _    _    _   _  ____ __  __    _    _   _ _ 
            | | | |  / \\  | \\ | |/ ___|  \\/  |  / \\  | \\ | | |
            | |_| | / _ \\ |  \\| | |  _| |\\/| | / _ \\ |  \\| | |
            |  _  |/ ___ \\| |\\  | |_| | |  | |/ ___ \\| |\\  |_|
            |_| |_/_/   \\_\\_| \\_|\\____|_|  |_/_/   \\_\\_| \\_(_)

--------------------------------------------------------------------------""")

    # Main menu listing
    while GAME_RUNNING:
        print(Fore.YELLOW + Back.MAGENTA + " 1) Play Game")
        print(Fore.YELLOW + Back.RED + " 2) Rules")        
        print(Fore.YELLOW + Back.BLUE + " 3) Exit Game")

        choice = input(Fore.GREEN + " Menu Select, enter desired number: \n" 
                       + Fore.WHITE)
        choice = choice.strip()
        
        if choice == "":
            mainMenu()
        # Play game option
        if (choice == "1"):
            getNumberOfPlayers()

        # Get rules option
        elif (choice == "2"):
            print(Fore.CYAN + f"""
            \n 1. Select Number of players (1-3 max).
            \n 2. Enter players names.
            \n 3. A word is generated at random.
            \n 4. Select letters you believe are in your random word. 
            \n 5. Keep guessing letters until you either guess the word or the 
hangman hangs!!!\n  
            ------------------------------------------------------\n""")
        # Exit option
        elif(choice == "3"):
            print(Fore.GREEN + " Thank you for playing!!!")
            GAME_RUNNING = False              
        else:
            # Check for invalid option
            print(Fore.RED + " Invalid Choice, Please Try Again.")


if __name__ == "__main__":
    # Display main menu
    #mainMenu()
    


    a = len("cp.letters_right = print_word(cp.random_word, cp.letters_guessed)")
    print(a)