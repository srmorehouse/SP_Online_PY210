#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Lesson 4, Exercise 3

@author: Matt Casari

Link: https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/mailroom-part2.html

Description:
    The Program: Part 2
    Update the program from Lesson 3 (Part 1) by using dicts where appropriate.

    Also, add file writing.

"""

DONORS = {}

PROMPT_TEXT = (
    "\nSelect an option:\n"
    "1. Send a Thank You to a single donor.\n"
    "2. Create a Report.\n"
    "3. Send letters to all donors.\n"
    "4. Quit\n"
    "> "
)


def prompt_user():

    switch_func_dict = {
        1: add_donor,
        2: generate_report,
        3: create_file,
        4: quit_program,
    }

    """ Prompts the user for menu option """

    result = input(PROMPT_TEXT)
    result = int(result)
    switch_func_dict.get(result)()


def initialize_donors():
    DONORS["Neil Armstrong"] = [15000.00, 15000.00]
    DONORS["Buzz Aldrin"] = [23021.10, 25020.30, 28999.29]
    DONORS["Sally Ride"] = [42917.42, 38281.28]
    DONORS["Al Shepard"] = [2387.00, 2321.42, 3700.00]
    DONORS["Alan Bean"] = [28477.13, 727.1]
    DONORS["Chris Hadfield"] = [17325.42, 13823.83, 0.99]


def calculate_stats(donations):
    # print(donor)
    """ Calculates the sum, average and number of donations for a donor """
    donor_sum = sum(donations)
    donor_num = len(donations)
    donor_average = donor_sum / donor_num
    return (donor_sum, donor_num, donor_average)


def sort_donors_by_total(name):
    """ Function used to sort donors by total contributions """
    return sum(DONORS[name])


def quit_program():
    """ 
    Exits out of program
    """
    print("Exiting Program")
    quit()


def create_file():
    pass


def generate_report():
    values = DONORS
    """ Generates a formatted report of donor names, total donation, # of donations and average donation """
    print("\n")
    column_donor_length = 0
    for value in values:
        column_donor_length = max(len(values),column_donor_length) + 5

    f_str = " {" + f":<{column_donor_length}" + "} | {} | {} | {}"
    title_str = f_str.format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print(title_str)
    print("-" * len(title_str))
 
    values = sorted(DONORS, key=sort_donors_by_total, reverse=True)

    for value in values:
        f_str = " {" + f":<{column_donor_length}" + "}  ${:11.2f}   {:9}  ${:12.2f}"
        (d_sum, d_num, d_ave) = calculate_stats(DONORS[value])
        v_str = f_str.format(value, d_sum, d_num, d_ave)
        
        print(v_str)


def print_donor_list(values):
    """ Prints the list of donors passed to function"""
    print("\nList of donors:".upper())
    for value in values:
        print(value)


def thank_you_email(name, amount):
    """
    Create the email from a template.
    
    Args:
        name: Name of donor
        amount: Amount donated (this time)
    Return:
        email: Contents of email
    """

    txt = (
        f"""\nDear {name},\n"""
        f"""Thank you for your recent donation of ${amount:.2f}. """
        f"""Your donation will help us purchase a taxidermied seagull.\n"""
        f"""Please consider donating again at your earliest convenience.\n\n"""
        f"""Sincerely,\n"""
        f"""The Human Fund\n"""
    )

    return txt


def add_donor():

    """ Adds new donor or new donation to existing donor """
    valid_donor = False
    while not valid_donor:
        donor = input("Enter Full Name (or list): ")

        for idx, value in enumerate(DONORS):
            if value[0] == donor:
                valid_donor = True
                break
        else:
            if donor == "list":
                print_donor_list(DONORS)
                continue
            else:
                DONORS[donor] = []

                idx += 1
                valid_donor = True
                break

    amount = input("Enter donation amount ($): ")
    amount = float(amount)

    # Add amount to data
    DONORS[donor].append(amount)

    txt = thank_you_email(donor, amount)
    print(txt)


def main():
    initialize_donors()
    """ Main Run Loop """
    while True:
        prompt_user()



if __name__ == "__main__":
    main()
