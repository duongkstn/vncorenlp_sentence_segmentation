class WordTag:
    def __init__(self, iword, itag):
        self.form = iword
        self.word = iword.lower()
        self.tag = itag