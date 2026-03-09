import random
from datetime import datetime
import pandas

# Functions begin here
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

def not_blank(question, error):
    """wrapper for input() that doesn't allow blank responses"""
    while True:
        response = input(question)
        if response != "":
            return response
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
    return f"{decoration * multiplier} {statement} {decoration * multiplier}"

def format_currency(x):
    return f"${x:.2f}"


# MAIN ROUTINE BEGINS HERE

print(styled_statement("MINI MOVIE FUNDRAISER", "*", 5))

# instructions
show_instructions = str_checker("Would you like to view the instructions? ", ["yes","no"],1,"Please enter yes or no.")

print()

# if the user wants to view instructions show them
if show_instructions == "yes":
    print(styled_statement("INSTRUCTIONS", "-", 3))
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

# ticket dict

mini_movie_dict = {
    "Name":         [],
    "Ticket Price": [],
    "Surcharge":    [],
}

while tickets_sold < MAX_TICKETS:
    name = not_blank("Name: ", "You must type a name!")

    # if name is blank, ask again
    if name == "":
        print("You must enter a name.")
        continue

    # break if exit code
    if name.lower() == "xxx":
        break

    age = int_check("Age: ", "You must enter an integer!")
    if 12 <= age <= 120:

        if age < 16:  # under 16 discount
            ticket_price = CHILD_PRICE
        elif age < 65:  # no discount
            ticket_price = ADULT_PRICE
        else:  # senior discount
            ticket_price = SENIOR_PRICE

        payment_method = str_checker("Payment method (cash/credit): ", ["cash", "credit"], 2, "Please enter cash or card.")

        # payment surcharge
        surcharge = 0

        if payment_method == "credit":
            surcharge = ticket_price * CREDIT_SURCHARGE

        mini_movie_dict["Name"].append(name)
        mini_movie_dict["Ticket Price"].append(ticket_price)
        mini_movie_dict["Surcharge"].append(surcharge)


        tickets_sold += 1
    elif age < 12 :
        print(f"{name} is too young.")
    elif age > 120:
        print(f"{name} is too old.")
    print()

print()
# create pandas frame and append total/profit columns to it

mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# pick random winner from names
winner = random.choice(mini_movie_dict["Name"])

# get the index of the winner to get their ticket cost from the dataframe
winner_index = mini_movie_dict["Name"].index(winner)

# ticket cost from the dataframe
winner_ticket_cost = mini_movie_frame.at[winner_index, "Ticket Price"] + mini_movie_frame.at[winner_index, "Surcharge"]

# zero out the winners ticket cost
mini_movie_frame.at[winner_index, "Ticket Price"] = 0
mini_movie_frame.at[winner_index, "Surcharge"] = 0

mini_movie_frame["Total"] = mini_movie_frame["Ticket Price"] + mini_movie_frame["Surcharge"]
mini_movie_frame["Profit"] = mini_movie_frame["Ticket Price"] - 5

# calculate total paid and profit
total_paid = mini_movie_frame["Total"].sum()
total_profit = mini_movie_frame["Profit"].sum()

# format everything to be $x
add_dollars = ["Total", "Surcharge", "Profit", "Ticket Price"]
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(format_currency)

mini_movie_string = mini_movie_frame.to_string(index=False)

if tickets_sold == MAX_TICKETS:
    tickets_sold_text = f"All {MAX_TICKETS} tickets were sold."
else:
    tickets_sold_text= f"{tickets_sold}/{MAX_TICKETS} tickets were sold."

winner_text = f"The lucky winner is {winner}! Their ticket worth ${winner_ticket_cost:.2f} is free!"
total_text = (f"\nTotal paid:   ${total_paid:.2f}"
      f"\nTotal profit: ${total_profit:.2f}\n")

print(tickets_sold_text)
print(winner_text)
print(mini_movie_string)
print(total_text)

# printing the receipt
receipt = str_checker("Would you like to save your receipt as a .txt file? ", ["yes","no"],1,"Please enter yes or no.")

print()

# if the user wants to view instructions show them
if receipt == "yes":
    # define filename
    file_name = "mmf_receipt"
    formatted_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    write_to = "{}_{}.txt".format(file_name, formatted_time)

    text_file = open(write_to, "w+")

    # list of strings to be included in the output of the file
    to_write = [
        styled_statement("Mini Movie Fundraiser Receipt", "=", 3),
        datetime.now().strftime("%d/%m/%Y %H:%M\n"),
        styled_statement("Ticket Details", "-", 3),
        mini_movie_string,
        total_text,
        "\n{}".format(styled_statement("Raffle Winner", "-", 4)),
        winner_text,
        "The ticket details have already been adjusted to take into account the winner.\n",
        tickets_sold_text
    ]

    # print to file
    for item in to_write:
        text_file.write(item)
        text_file.write("\n")

