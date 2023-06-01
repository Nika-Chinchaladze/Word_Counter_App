"""Module is responsible for executing console based 'word_counter_project' application,
module uses classes from file_handler and text_handler modules.
"""

from file_handler import FileHandler
from text_handler import TextHandler
from app_rules import APPLICATION_RULES


def word_counter_project():
    """function counts desired word in provided text input or in .txt file."""

    # Greeting message in the beginning of the application.
    print(f"Welcome to word counter console based application!\n<-{'='*70}->")

    # Here we suggest user to check existing rules - how to use our app.
    rules = input("Do you want to see the rules, how to use application: yes/no -> ").strip().lower()
    if rules == "yes":
        print(APPLICATION_RULES)
    else:
        print(f"Seems you already know, how to use our application, VERY GOOD!\n{'-'*74}")

    # Here we will provide user with two available choices, where
    # He is going to count word quantity: in entered string or in some
    # Specified .txt file. We will use while loop, which stops only when
    # User enters correct answer / correct choice or enters special keyword: 'stop'.
    correct_input = False
    while not correct_input:
        user_choice = input("Where are you searching word quantity, choose one: input or file! -> ").strip().lower()

        # Based on user input we will execute specific action.
        # Here user can stop the program running process - manually!
        if user_choice == "stop":
            print("You have stopped the execution of program, Thank you for being with us!")
            correct_input = True
            return correct_input

        # If user chooses 'file' then program will use LargeFileHandler class
        elif user_choice == "file":
            correct_input = True
            tool_1 = FileHandler()

            # Here user must provide correct file path, to get the quantity of desired word
            # If user want's to stop the process, he must enter special keyword -'stop', instead of file path.
            correct_file_path = False
            while not correct_file_path:
                provided_file_path = input("Please enter target file path: -> ").lower()

                # Here user will stop the program running process - manually.
                if provided_file_path == "stop":
                    print("You have stopped the execution of program, Thank you for being with us!")
                    correct_file_path = True
                    return correct_file_path

                # Here we check if file provided by user, exists on pointed location.
                # If file exists, then program will split it - in chunks and then return the quantity
                # Of desired word occurrences.
                if tool_1.check_file_existence(file_path=provided_file_path):
                    correct_file_path = True
                    provided_word_1 = input("Please enter desired word, which quantity will be counted: -> ").lower()
                    result_1 = tool_1.count_word_quantity(file_path=provided_file_path, word=provided_word_1)
                    if result_1 is not None:
                        print(f"Total Quantity: {result_1}")
                        return result_1
                else:
                    print(">>> File with that name doesn't exist on pointed location!")

        # If user chooses 'input' then program will use TextHandler class
        elif user_choice == "input":
            correct_input = True
            provided_text = input("Please enter text, in which you going to count word quantity: -> ").lower()
            provided_word_2 = input("Please enter desired word, which quantity will be counted: -> ").lower()
            tool_2 = TextHandler()
            result_2 = tool_2.count_word_quantity(text=provided_text, word=provided_word_2)
            if result_2 is not None:
                print(f"Total Quantity: {result_2}")
                return result_2

        # If code reaches this place it means that user entered wrong answer,
        # Program will repeat the question again, with possible answers,
        # User will be able to continue the process, only when he enters one from the
        # Available choices.
        else:
            print(">>> Please enter only one of them: input or file!")


if __name__ == "__main__":
    word_counter_project()
