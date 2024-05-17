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
