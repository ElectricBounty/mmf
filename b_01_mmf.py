# DEFINES BEGIN HERE

def str_checker(question, available_choices, num_letters, error):
    """returns the string if it meets anything in available_choices"""
    while True:
        choice = input(question).lower()
        for item in available_choices:

            if choice == item:
                return item

            # check first num_letters of letters to see if they tried to write the answer
            elif choice == item[:num_letters]:
                return item

        print(error)

def num_check(question, error, num_type, exitcode=None):
    """Catches any numbers that are invalid or in a range, allow programmer to set num_type"""

    # define change_to variable as either the int function or the float function
    if num_type == "int":
        change_to = int
    else:
        change_to = float

    while True:
        try:
            # ask user for a number
            response = input(question)
            if response.lower() == exitcode:
                return exitcode
            return change_to(response)

        # checks that number is valid
        except ValueError:
            print(error)

def styled_statement(statement, decoration, multiplier):
    """Displays a statement with a certain number of decorations on each side"""
    print(f"\n{decoration * multiplier} {statement} {decoration * multiplier}")

def styled_instructions(symbol, array):
    """takes an array of sentences and formats them into a bullet-pointed list"""

    # iterate through array and print items with a
    for item in array:
        print(f"{symbol} {item}")


# MAIN ROUTINE BEGINS HERE

styled_statement("MINI MOVIE FUNDRAISER", "*", 5)

# instructions
show_instructions = str_checker("Would you like to view the instructions? ", ["yes","no"],1,"Please enter yes or no.")

print()

# if the user wants to view instructions show them
if show_instructions == "yes":
    styled_statement("INSTRUCTIONS", "-", 3)
    styled_instructions("-",[
        "Enter each ticket holder's name, age and payment ",
        "instruction 2",
        "instruction 3",
        "have fun buying tickets??"
    ])
    print('''For each ticket holder enter ...
- Their name
- Their age
- Their payment method

The program will record the ticket sale and calculate the ticket cost (and profit).

Once you have entered all of the tickets, or entered the exit code (xxx), the program will display
the ticket sales information and write the data to a text file.

It will also choose one lucky ticket winner who wins the draw (their ticket is free).
    ''')

# begin program

# init ticket numbers

MAX_TICKETS = 5
tickets_sold = 0

# loop for selling tickets
while tickets_sold < MAX_TICKETS:
    name = input("Name: ")

    # break if exit code
    if name.lower() == "xxx":
        break

    tickets_sold += 1

if tickets_sold == MAX_TICKETS:
    print(f"All {MAX_TICKETS} tickets have been sold.")
else:
    print(f"{tickets_sold}/{MAX_TICKETS} tickets have been sold.")