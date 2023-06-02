"""Module contains PunctuationHandler class that contains replace_punctuations method."""

import string


class BaseHandler:
    """class contains replace_punctuations method."""

    def replace_punctuations(self, text) -> str:
        """methods replaces every punctuation with empty string"""
        # Here we iterated through punctuation symbols
        # And replace them with empty string
        for character in string.punctuation:
            text = text.replace(character, "")
        return text.strip().lower().split()
