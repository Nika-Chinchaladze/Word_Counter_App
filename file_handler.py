"""module is responsible for handling large files, by splitting it in multiple sub-files,
and then serving them.
"""

import os
import string

from filesplit.split import Split


class LargeFileHandler:
    """class is responsible for handling large files"""

    def __init__(self):
        self.split_directory = "split_files"

    def check_file_existence(self, file_path):
        if os.path.isfile(file_path) and file_path.endswith(".txt"):
            return True
        return False

    def split_file(self, file_path):
        """method splits file into smaller chunks into specified directory"""
        try:
            my_split = Split(inputfile=file_path, outputdir=self.split_directory)
            my_split.bysize(size=10240, newline=False, includeheader=False)
            return True
        except FileNotFoundError:
            return False

    def clean_split_files_directory(self):
        """method cleans split files directory from existing files."""
        for file in os.listdir(path=self.split_directory):
            os.remove(os.path.join(self.split_directory, file))
        return len(os.listdir(path=self.split_directory))

    def get_file_name_list(self):
        """method returns list of file_name from specified directory"""
        result = []
        for path in os.listdir(path=self.split_directory):
            if os.path.isfile(os.path.join(self.split_directory, path)):
                if path.endswith(".txt"):
                    result.append(path)
        return result

    def replace_punctuation(self, line):
        """methods replaces every punctuation with empty string"""
        for character in string.punctuation:
            line = line.replace(character, "")
        return line

    def count_word_quantity(self, file_path, word):
        """methods iterates through provided list of .txt files
        And counts the quantity of provided word
        """
        if self.split_file(file_path=file_path):
            quantity = 0
            file_list = self.get_file_name_list()
            if len(file_list) > 0:
                for file in file_list:
                    with open(f"{self.split_directory}/{file}", "r", encoding="utf8") as my_file:
                        for line in my_file:
                            my_line = self.replace_punctuation(line=line.strip()).lower()
                            my_words_list = my_line.split()
                            if len(my_words_list) > 0:
                                quantity += my_words_list.count(word.lower())
                        my_file.close()
            self.clean_split_files_directory()
            return quantity
