class Player():
    def __init__(self, firstname):
        self.name = firstname
        self.wordtoguess = ""
        self.amount_of_times_wrong = 0
        self.random_word = ""
        
        
        self.length_of_word_to_guess = 0

        self.current_guess_index = 0
        self.current_letters_guessed = []
        self.current_letters_right = 0

        self.amount_of_times_wrong = 0
        self.GAME_OVER = False
        
        self.colours = {}
        
    def set_word(self, random_word):
        self.random_word = random_word
        self.length_of_word_to_guess = len(random_word)
    
    def print_word(self):
        print (self.random_word)
        return self.random_word

    def set_colour(self, palette):
        self.colours = palette