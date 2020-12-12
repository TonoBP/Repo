class WOFPlayer:

    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []

    def addMoney(self, amt):
        self.prizeMoney = self.prizeMoney + amt

    def goBankrupt(self):
        self.prizeMoney = 0

    def addPrize(self, prize):
        self.prizes.append(prize)

    def __str__(self):
        return "{} (${})".format(self.name, self.prizeMoney)
class WOFHumanPlayer(WOFPlayer):

    def getMove(category, obscuredPhrase, guessed):
        move = input(status)
        status = """
        Category: {}
        Phrase: {}
        Guessed: {}

        Guess a letter, phrase, or type 'exit' or 'pass': """.format(category, obscuredPhrase, guessed)
class WOFComputerPlayer(WOFPlayer):

    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    def __init__ (self, name, difficulty):
        WOFPlayer.__init__(self, name)
        self.difficulty = difficulty

    def smartCoinFlip(self):
        coin = random.randint(1, 10)
        if coin > self.difficulty:
            return True
        else:
            return False

    def getPossibleLetters(self, guessed):
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        VOWELS = "AEIOU"
        CanBeGuessed = []
        for letter in LETTERS:
            if letter not in guessed and letter not in VOWELS:
                CanBeGuessed.append(letter)
            elif letter not in guessed and letter in VOWELS:
                if self.prizeMoney >250:
                    CanBeGuessed.append(letter)
        return CanBeGuessed

    def getMove(self, category, obscuredPhrase, guessed):
        CanBeGuessed = self.getPossibleLetters(guessed)

        if CanBeGuessed == []:
            return 'pass'

        else:
            move = self.smartCoinFlip()
            if move == True:    #ver qué lst_letters aínda están en frequencies_lst e devolver a última
                i = len(self.SORTED_FREQUENCIES)-1
                while(0 <= i <= len(self.SORTED_FREQUENCIES)-1):
                    if self.SORTED_FREQUENCIES[i] in CanBeGuessed:
                        return self.SORTED_FREQUENCIES[i]
                    else:
                        i-=1
                        continue
            else:
                return random.choice(CanBeGuessed)
