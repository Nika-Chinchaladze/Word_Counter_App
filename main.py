from file_handler import LargeFileHandler
from text_handler import TextHandler


def word_counter_project():
    """function counts desired word in provided text input or in .txt file."""

    # Greeting message in the beginning of the application.
    print("Welcome to word counter console based application!")

    # Here we will provide user with two available choices, where
    # He is going to count word quantity: in entered string or in some
    # Specified .txt file. We will use while loop, which stops only when
    # User enters correct answer / correct choice.
    correct_input = False
    while not correct_input:
        user_choice = input("Where are you searching word quantity: in input or in file, choose one! ").lower()

        # Based on user input we will execute specific action.
        # If user chooses 'file' then program will use LargeFileHandler class
        if user_choice == "file":
            correct_input = True
            tool_1 = LargeFileHandler()

        # If user chooses 'input' then program will use TextHandler class
        elif user_choice == "input":
            correct_input = True
            provided_text = input("Please enter text, where are you going to count word quantity! ").lower()
            provided_word = input("Please enter desired word, which quantity will be counted! ").lower()
            tool_2 = TextHandler()
            result_2 = tool_2.count_word_quantity(text=provided_text, word=provided_word)
            print(result_2)

        # If code reaches this place it means that user entered wrong answer,
        # Program will repeat the question again, with possible answers,
        # User will be able to continue the process, only when he enters one from the
        # Available choices.
        else:
            print("Please enter only one of them: input or file!")


if __name__ == "__main__":
    word_counter_project()
