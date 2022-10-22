class FWObject:
    """
    Define a 5-word/tag window object to capture the context surrounding a word.
    """
    def __init__(self, check):
        if check:
            self.context = ["<W>", "<T>","<W>", "<T>","<W>", "<T>","<W>", "<T>","<W>", "<T>"]
        else:
            self.context = [""] * 10
