"""Module represents collection of rules, how word_counter_application can be used"""


APPLICATION_RULES = """
1. In the beginning user must choose, from where is he/she going to get quantity of word occurrences: from user input
or from specific .txt file. Also user can type special keyword - 'stop' - to stop the running process of application,
if he/she doesn't want to continue the process.

2. If user chose option - 'input', then program will ask him/her to enter some string.

3. After entering string - program will ask for - 'word', which quantity of occurrences will be counted in the provided
string.

4. If user chose option - 'file', then program will ask him/her to enter valid path to target file.
for example: "D://test_file.txt"

5. Program will check if provided path is valid and file really exists, and only then asks user to enter - desired word,
that quantity will be counted in targeted file. If file doesn't exist, then program will show informative warning to
user and asks to re-define the correct path again. Here user can type special keyword - 'stop' - to stop the execution
process of word_counter_application.

<-==================================================================================================================->
"""
