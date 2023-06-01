"""Module tests TextHandler and LargeFileHandler class methods, also module is
responsible for testing 'word_counter_project' function from main.py
"""

import os
import sys
import shutil
import unittest

from unittest.mock import patch

from text_handler import TextHandler
from file_handler import FileHandler
from punctuation_handler import PunctuationHandler
from main import word_counter_project


class TestTextHandler(unittest.TestCase):
    """Test methods of TextHandler class methods."""

    @classmethod
    def setUpClass(cls):
        cls.my_tool = TextHandler()

    def test_count_word_quantity(self):
        """Tests count_word_quantity method of TextHandler class."""
        my_text_1 = "I love Python python python!!!"
        my_text_2 = "Red, blue"
        my_word_1 = "python"
        my_word_2 = "green"
        my_result_1 = self.my_tool.count_word_quantity(text=my_text_1, word=my_word_1)
        my_result_2 = self.my_tool.count_word_quantity(text=my_text_2, word=my_word_2)
        self.assertEqual(my_result_1, 3)
        self.assertEqual(my_result_2, 0)


class TestFileHandler(unittest.TestCase):
    """Tests LargeFileHandler class methods."""

    @classmethod
    def setUpClass(cls):
        cls.my_tool = FileHandler()
        # Create directory and .txt file with content
        os.makedirs("data_directory")
        with open("data_directory/data_file.txt", "w") as file:
            file.write(f"{'java '*1000}\n{'css '*15}\n{'ruby '*3000}\n{'css '*5}")
            file.close()

    @classmethod
    def tearDownClass(cls):
        # Remove directory if exists
        if os.path.exists(path="data_directory"):
            shutil.rmtree(path="data_directory", ignore_errors=True)

    def test_check_file_existence_success(self):
        """Tests check_file_existence method of FileHandler class on success situation"""
        my_result = self.my_tool.check_file_existence(file_path="data_directory/data_file.txt")
        self.assertTrue(my_result)

    def test_check_file_existence_error(self):
        """Tests check_file_existence method of FileHandler class on error situation"""
        my_result = self.my_tool.check_file_existence(file_path="data_directory/tommy.txt")
        self.assertFalse(my_result)

    def test_read_chunks(self):
        """Tests read_chunk method of FileHandler class."""
        with open("data_directory/data_file.txt", "r", encoding="utf8") as file:
            for chunk in self.my_tool.read_chunks(file_object=file):
                self.assertLessEqual(a=sys.getsizeof(chunk), b=2048)

    def test_count_word_quantity_success(self):
        """Tests count_word_quantity method of FileHandler class on success."""
        my_result = self.my_tool.count_word_quantity(file_path="data_directory/data_file.txt", word="css")
        self.assertEqual(my_result, 20)

    def test_count_word_quantity_error(self):
        """Tests count_word_quantity method of FileHandler class on error."""
        my_result = self.my_tool.count_word_quantity(file_path="data_directory/tommy.txt", word="shelby")
        self.assertFalse(my_result)


class TestPunctuationHandler(unittest.TestCase):
    """Tests PunctuationHandler class."""

    def setUp(self) -> None:
        self.my_tool = PunctuationHandler()

    def test_replace_punctuations(self):
        """Tests replace_punctuations method of PunctuationHandler class."""
        my_text = "My Favourite Languages: py!thON, HT??ml, Cs+s, Java!!!!"
        my_result = ["my", "favourite", "languages", "python", "html", "css", "java"]
        final_result = self.my_tool.replace_punctuations(text=my_text)
        self.assertEqual(final_result, my_result)


class TestWordCounterProject(unittest.TestCase):
    """Tests console based word_counter_project function."""

    @classmethod
    def setUpClass(cls):
        cls.text_handler_tool = TextHandler()
        cls.file_handler_tool = FileHandler()
        # Create directory and .txt file with content
        os.makedirs("data_directory")
        with open("data_directory/data_file.txt", "w") as file:
            file.write(f"{'java ' * 1000}\n{'css ' * 15}\n{'ruby ' * 3000}\n{'css ' * 5}")
            file.close()

    @classmethod
    def tearDownClass(cls):
        # Remove directory if exists
        if os.path.exists(path="data_directory"):
            shutil.rmtree(path="data_directory", ignore_errors=True)

    @patch("builtins.input")
    def test_a_stop_choice(self, mock_user_choice):
        """Tests if execution of function stops / breaks, when user enters special keyword - stop"""
        mock_user_choice.return_value = "stop"
        self.assertTrue(word_counter_project())

    @patch("builtins.input")
    def test_file_choice(self, mock_user_choice_file):
        """Tests if function returns correct quantity of word occurrences,
        when user decides to count word's quantity in specific .txt file.
        """
        mock_user_choice_file.return_value = "file"
        my_file_path = "data_directory/data_file.txt"
        my_word = "css"
        my_result = self.file_handler_tool.count_word_quantity(file_path=my_file_path, word=my_word)
        self.assertEqual(my_result, 20)

    @patch("builtins.input")
    def test_input_choice(self, mock_user_choice_input):
        """Tests if function returns correct quantity of occurrences,
        when user decides to count word's quantity in provided string.
        """
        mock_user_choice_input.return_value = "input"
        my_text = "I love programing: python, PYTHON, PYthon, pyTHon!!!"
        my_word = "PyThoN"
        my_result = self.text_handler_tool.count_word_quantity(text=my_text, word=my_word)
        self.assertEqual(my_result, 4)


if __name__ == "__main__":
    unittest.main()
