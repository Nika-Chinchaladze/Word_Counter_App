"""Module tests TextHandler and LargeFileHandler class methods, also module is
responsible for testing 'word_counter_project' function from main.py
"""

import unittest

from unittest.mock import patch
from text_handler import TextHandler
from file_handler import LargeFileHandler
from main import word_counter_project


class TestTextHandler(unittest.TestCase):
    """Test methods of TextHandler class methods."""

    @classmethod
    def setUpClass(cls):
        cls.my_tool = TextHandler()

    def test_1_replace_punctuations(self):
        """Tests replace_punctuations method of TextHandler class."""
        my_text = "I, love, programming!!!"
        my_result = self.my_tool.replace_punctuantions(text=my_text)
        self.assertEqual(my_result, "I love programming")

    def test_2_count_word_quantity(self):
        """Tests count_word_quantity method of TextHandler class."""
        my_text_1 = "I love Python python python!!!"
        my_text_2 = "Red, blue"
        my_word_1 = "python"
        my_word_2 = "green"
        my_result_1 = self.my_tool.count_word_quantity(text=my_text_1, word=my_word_1)
        my_result_2 = self.my_tool.count_word_quantity(text=my_text_2, word=my_word_2)
        self.assertEqual(my_result_1, 3)
        self.assertEqual(my_result_2, 0)


class TestLargeFileHandler(unittest.TestCase):
    """Tests LargeFileHandler class methods."""

    @classmethod
    def setUpClass(cls):
        cls.my_tool = LargeFileHandler()

    def test_1_check_file_existence_error(self):
        """Tests check_file_existence method of LargeFileHandler class on error situation"""
        my_result = self.my_tool.check_file_existence(file_path="tommy.txt")
        self.assertFalse(my_result)

    def test_2_check_file_existence_success(self):
        """Tests check_file_existence method of LargeFileHandler class on success situation"""
        my_result = self.my_tool.check_file_existence(file_path="data.txt")
        self.assertTrue(my_result)

    def test_3_split_file_method_error(self):
        """Tests split_file method of LargeFileHandler class on error situation."""
        my_result = self.my_tool.split_file(file_path="tommy.txt")
        self.assertFalse(my_result)

    def test_4_split_file_method_success(self):
        """Tests split_file method of LargeFileHandler class on success situation."""
        my_result = self.my_tool.split_file(file_path="data.txt")
        self.assertTrue(my_result)

    def test_5_get_file_name_list(self):
        """Tests get_file_name_list method of LargeFileHandler class."""
        my_files_list = self.my_tool.get_file_name_list()
        my_check = []
        for file in my_files_list:
            if file.startswith("data") and (file.endswith(".txt")):
                my_check.append(True)
        self.assertEqual(len(my_check), len(my_files_list))
        self.assertNotIn(False, my_check)

    def test_6_clean_split_files_directory(self):
        """Tests clean_split_files_directory method of LargeFileHandler class."""
        my_result = self.my_tool.clean_split_files_directory()
        self.assertEqual(my_result, 0)

    def test_7_replace_punctuations(self):
        """Tests replace_punctuations method of LargeFileHandler class."""
        my_text = "I, l#ov*e, pr#og%ram?ming!!!"
        my_result = self.my_tool.replace_punctuation(line=my_text)
        self.assertEqual(my_result, "I love programming")

    def test_8_count_word_quantity_success(self):
        """Tests count_word_quantity method of LargeFileHandler class on success."""
        my_result = self.my_tool.count_word_quantity(file_path="data.txt", word="shelby")
        self.assertEqual(my_result, 5)

    def test_9_count_word_quantity_error(self):
        """Tests count_word_quantity method of LargeFileHandler class on error."""
        my_result = self.my_tool.count_word_quantity(file_path="tommy.txt", word="shelby")
        self.assertFalse(my_result)


class TestWordCounterProject(unittest.TestCase):
    """Tests console based word_counter_project function."""

    @classmethod
    def setUpClass(cls):
        cls.text_handler_tool = TextHandler()
        cls.file_handler_tool = LargeFileHandler()

    @patch("builtins.input")
    def test_1_user_choice(self, mock_user_choice):
        """Tests if execution of function stops / breaks, when user enters special keyword - stop"""
        mock_user_choice.return_value = "stop"
        self.assertTrue(word_counter_project())

    @patch("builtins.input")
    def test_2_user_choice_input(self, mock_user_choice_input):
        """Tests if function returns correct quantity of occurrences,
        when user decides to count word's quantity in provided string.
        """
        mock_user_choice_input.return_value = "input"
        my_text = "I love programing: python, PYTHON, PYthon, pyTHon!!!"
        my_word = "PyThoN"
        my_result = self.text_handler_tool.count_word_quantity(text=my_text, word=my_word)
        self.assertEqual(my_result, 4)

    @patch("builtins.input")
    def test_3_user_choice_file(self, mock_user_choice_file):
        """Tests if function returns correct quantity of word occurrences,
        when user decides to count word's quantity in specific .txt file.
        """
        mock_user_choice_file.return_value = "file"
        my_file_path = "data.txt"
        my_word = "shelby"
        my_result = self.file_handler_tool.count_word_quantity(file_path=my_file_path, word=my_word)
        self.assertEqual(my_result, 5)


if __name__ == "__main__":
    unittest.main()
