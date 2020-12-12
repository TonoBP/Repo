class WOFHumanPlayer(WOFPlayer):

    def getMove(category, obscuredPhrase, guessed):
        move = input(status)
        status = """
        Category: {}
        Phrase: {}
        Guessed: {}

        Guess a letter, phrase, or type 'exit' or 'pass': """.format(category, obscuredPhrase, guessed)
