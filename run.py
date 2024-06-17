import os
import random
import string
from words import words
from colorama import init, Fore, Back, Style
from player import Player

# initialise colorama library
init(autoreset=True)

""" Create palatte for players colours """
palettes = [
    {
        'prompt': Fore.YELLOW,
        'win': Fore.YELLOW + Back.CYAN,
        'lose': Fore.BLACK + Back.RED,
    }, {
        'prompt': Fore.GREEN,
        'win': Fore.YELLOW + Back.GREEN,
        'lose': Fore.BLACK + Back.RED,
    }, {
        'prompt': Fore.BLUE,
        'win': Fore.YELLOW + Back.GREEN,
        'lose': Fore.BLACK + Back.RED,
    }
]

""" Store whitespace and invalid characters in input prompts. """
punct = string.punctuation + " "
numbers = "0123456789"
tries = 9
# Concatenate all invalid input for game
invalid_chars = punct + numbers


""" function for adding player name """


def add_player(name):
    p = Player(name)
    players.append(p)
    return p


""" function for checking invalid characters """


def check_valid(char):
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

""" Display player word and letters guessed so far """


def print_word(word, guessed_letters):
    right_letters = 0
    display_word = ""
    # loop to print correct letters in word
    for char in word:
        if char in guessed_letters:
            display_word += char + ' '
            right_letters += 1
        else:
            display_word += '_ '
    print(display_word.strip())
    return right_letters


"""function to get word"""


def get_word():
    # pick a random word from list
    word = random.choice(words)
    return word


"""Runs the game"""


def run():
    while (True):
        if len(players) == 0:
            main_menu()

        for p in range(len(players)):
            # Add boundary between player goes/players
            print("\n %s %s %s " % ("=" * 20, " NEXT PLAYER ", "=" * 20))
            # Set current player
            cp = players[p]

            print(cp.colours['prompt'] +
                  "\n Your turn %s!" % (cp.name))
            print_word(cp.word, cp.letters_guessed)

            # Check for game over state
            if cp.amount_of_times_wrong >= tries:
                cp.GAME_OVER = True
                print(cp.colours['lose'] + " GAME OVER! %s :( " % (cp.name))
                print(cp.colours['lose'] + " Your word was...")
                print(cp.colours['prompt'] + cp.word)
                players.pop(p)
                break

            # Check for win state
            if cp.letters_right >= cp.length_of_word_to_guess:
                print(cp.colours['win'] + " YOU WONNN!")
                players.pop(p)

                # Show player names and words if game over
                for losing_player in players:
                    print(losing_player.colours['lose'] +
                          " %s, your word was..." % (losing_player.name))
                    print(losing_player.colours['prompt'] +
                          losing_player.word)

                # Call main menu
                main_menu()

            # Display letters guessed so far for current player
            if len(cp.letters_guessed) >= 1:
                print(cp.colours['prompt'] + "\n Letters guessed so far: ")

            for letter in cp.letters_guessed:
                print(cp.colours['prompt'] + letter, end="  ")

            # prompt for user input
            letter_guessed = input(cp.colours['prompt'] +
                                   "\n Guess a letter (attempts left=%d): "
                                   % (tries - cp.amount_of_times_wrong))

            # check for multiple characters entered at once
            if len(letter_guessed) > 1:
                print(cp.colours['prompt'] +
                      "\n No more than one character allowed")
                run()
            # Check for valid characters
            is_valid = check_valid(letter_guessed)

            if not is_valid or letter_guessed == "":
                print(cp.colours['prompt'] + Fore.RED +
                      "\n Valid characters are A-Z & a-z," +
                      "No special characters allowed")
                run()

            # Check if letter already guessed
            if letter_guessed in cp.letters_guessed:
                print(cp.colours['prompt'] +
                      " You already guessed '%s'" % (letter_guessed))
                run()
            # User is right
            for cp.guess_index in range(cp.length_of_word_to_guess):
                if cp.word[cp.guess_index] == letter_guessed:
                    cp.letters_guessed.append(letter_guessed)
                    cp.letters_right = print_word(cp.word, cp.letters_guessed)
                    break
            # User wrong
            if (cp.word[cp.guess_index] != letter_guessed):
                if (cp.letters_right < cp.length_of_word_to_guess):
                    cp.amount_of_times_wrong += 1
                    cp.letters_guessed.append(letter_guessed)
                    # Update drawing
                    print_hangman(cp.amount_of_times_wrong)
                    # Print word
                    cp.letters_right = print_word(cp.word, cp.letters_guessed)


""" Main game menu loop """


def get_player_names():
    print(Fore.GREEN + "Enter player name:" + Fore.WHITE)
    name = input()

    name = name.lstrip().rstrip()
    if name == "":
        print("Not a valid player name! Please try again.")
        get_player_names()
    return name


# Get number of players
def get_number_of_players():
    print(Fore.GREEN + " Enter number of players: (1-3 max)")
    player_num = input()

    # Check for invalid characters
    if player_num in punct or player_num == "":
        print(Fore.RED + " Not a valid number! Please try again.")
        get_number_of_players()
    # Set number of players
    player_num = int(player_num)

    # Check number is in range of 1 to 3 and not less than 0
    if player_num <= 0:
        print(Fore.RED + " The min number of players is 1! Try again.")
        get_number_of_players()
    # Check number is in range of 1 to 3 and not greater than 3
    elif player_num > 3:
        print(Fore.RED + " The max number of players is 3! Try again.")
        get_number_of_players()
    else:
        # Get name and word for each player
        print(Fore.GREEN + " Number of players:" + Fore.WHITE, player_num)
        for p in range(player_num):

            # Initialise player
            name = get_player_names()
            player = add_player(name)
            word = get_word()
            player.set_word(word)
            player.set_colour(palettes[p])

        # Corrected bug in multiplayer option
        print(Fore.GREEN + " Let's Playyyyyyy!!!")
    # Run game
    run()


"""Main menu"""


def main_menu():

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
            main_menu()
        # Play game option
        if (choice == "1"):
            get_number_of_players()

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
        elif (choice == "3"):
            print(Fore.GREEN + " Thank you for playing!!!")
            GAME_RUNNING = False
        else:
            # Check for invalid option
            print(Fore.RED + " Invalid Choice, Please Try Again.")


if __name__ == "__main__":
    # Display main menu
    main_menu()
