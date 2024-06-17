class Player():
    def __init__(self, firstname):
        self.name = firstname.upper()
        self.wordtoguess = ""
        self.amount_of_times_wrong = 0
        self.word = ""
        
        
        self.length_of_word_to_guess = 0

        self.guess_index = 0
        self.letters_guessed = []
        self.letters_right = 0

        self.amount_of_times_wrong = 0
        self.GAME_OVER = False
        
        self.colours = {}
        
    def set_word(self, word):
        self.word = word
        self.length_of_word_to_guess = len(word)
    
    def print_word(self):
        print (self.word)
        return self.word

    def set_colour(self, palette):
        self.colours = palette