"""Module is responsible for handling large files, by splitting it in multiple sub-files,
and then serving them.
"""

from __future__ import annotations

import os

from punctuation_handler import PunctuationHandler


class FileHandler(PunctuationHandler):
    """class is responsible for handling large files"""

    def __init__(self):
        super().__init__()
        self.__chunk_size = 1024

    def check_file_existence(self, file_path) -> bool:
        """method checks if file really exists on pointed location."""
        # Here we check on file existence and if it is .txt file.
        if os.path.isfile(file_path) and file_path.endswith(".txt"):
            return True
        return False

    def read_chunks(self, file_object) -> str:
        """method yields small chunks from provided file"""
        while True:
            chunk = file_object.read(self.__chunk_size)
            if not chunk:
                break
            yield chunk

    def count_word_quantity(self, file_path, word) -> int | bool:
        """method iterates through provided list of .txt files
        And counts the quantity of provided word
        """
        if self.check_file_existence(file_path=file_path):
            quantity = 0
            # Here we iterate though chunks and count occurrences of provided word.
            with open(file_path, "r", encoding="utf8") as file:
                for chunk in self.read_chunks(file_object=file):
                    quantity += super().replace_punctuations(text=chunk).count(word.lower())
            return quantity
        return False
