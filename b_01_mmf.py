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

def int_check(question, error):
    """only accept integers"""

    while True:
        try:
            # ask user for a number
            response = input(question)

            return int(response)

        # checks that number is valid
        except ValueError:
            print(error)

def styled_statement(statement, decoration, multiplier):
    """Displays a statement with a certain number of decorations on each side"""
    print(f"{decoration * multiplier} {statement} {decoration * multiplier}")


# MAIN ROUTINE BEGINS HERE

styled_statement("MINI MOVIE FUNDRAISER", "*", 5)

# instructions
show_instructions = str_checker("Would you like to view the instructions? ", ["yes","no"],1,"Please enter yes or no.")

print()

# if the user wants to view instructions show them
if show_instructions == "yes":
    styled_statement("INSTRUCTIONS", "-", 3)
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

# init constants
CHILD_PRICE     = 7.50
ADULT_PRICE     = 10.50
SENIOR_PRICE    = 6.50

MAX_TICKETS     = 5

CREDIT_SURCHARGE = 0.05 # 5% surcharge for purchasing tickets with credit

# loop for selling tickets
tickets_sold = 0

while tickets_sold < MAX_TICKETS:
    name = input("Name: ")

    # if name is blank, ask again
    if name == "":
        print("You must enter a name.")
        continue

    # break if exit code
    if name.lower() == "xxx":
        break

    age = int_check("Age: ", "You must enter an integer!")
    if 12 <= age <= 120:
        payment_method = str_checker("Payment method (cash/credit): ", ["cash", "credit"], 2, "Please enter cash or card.")

        print(f"{name} bought a ticket. ({payment_method})")

        tickets_sold += 1
    elif age < 12 :
        print(f"{name} is too young.")
    elif age > 120:
        print(f"{name} is too old.")
    else:
        pass
    print()

print()
if tickets_sold == MAX_TICKETS:
    print(f"All {MAX_TICKETS} tickets have been sold.")
else:
    print(f"{tickets_sold}/{MAX_TICKETS} tickets have been sold.")