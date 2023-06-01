"""Module contains TextHandler class that is responsible for counting the quantity of
specified word in provided text.
"""

from punctuation_handler import PunctuationHandler


class TextHandler(PunctuationHandler):
    """class is responsible for counting desired word occurrence quantity in provided text."""

    def __init__(self):
        super().__init__()
        self.__hello = None

    def count_word_quantity(self, text, word) -> int:
        """method counts quantity of specified word in provided text."""
        quantity = 0
        # Here we replace punctuations with empty string and make list of words
        # By splitting provided string into separated words.
        my_text = super().replace_punctuations(text=text)
        if len(my_text) > 0:
            quantity += my_text.count(word.lower())
        return quantity
