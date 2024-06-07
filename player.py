class Player():
    def __init__(self, firstname):
        self.name = firstname
        self.wordtoguess = ""
        self.amount_of_times_wrong = 0
        self.randomWord = ""
        
        
        self.length_of_word_to_guess = 0

        self.current_guess_index = 0
        self.current_letters_guessed = []
        self.current_letters_right = 0

        self.amount_of_times_wrong = 0
        self.GAME_OVER = False
        
        self.colours = {}
        
    def setWord(self, randomWord):
        self.randomWord = randomWord
        self.length_of_word_to_guess = len(randomWord)
    
    def printWord(self):
        print (self.randomWord)
        return self.randomWord

    def setColour(self, palette):
        self.colours = palette