"""Module contains TextHandler class that is responsible for counting the quantity of
specified word in provided text.
"""

import string


class TextHandler:
    """class is responsible for counting desired word occurrence quantity in provided text."""

    def __init__(self):
        self.hello = None

    def replace_punctuantions(self, text):
        """methods replaces every punctuation with empty string"""
        # Here we iterated through punctuation symbols
        # And replace them with empty string
        for character in string.punctuation:
            text = text.replace(character, "")
        return text

    def count_word_quantity(self, text, word):
        """method counts quantity of specified word in provided text."""
        quantity = 0
        # Here we replace punctuations with empty string and make list of words
        # By splitting provided string into separated words.
        my_text = self.replace_punctuantions(text=text).strip().lower().split()
        if len(my_text) > 0:
            quantity += my_text.count(word.lower())
        return quantity

