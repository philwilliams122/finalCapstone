# This program allows the user to access two different financial calculators:
# an investment calculator and a home loan repayment calculator.
import math

# This part of the program asks the user to select which calculator they would like to access.
print("investment - to calculate the amount of interest you'll earn on your investment ")
print("bond - to calculate the amount of interest you'll have to pay on a home loan ")

choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
choice_lower = choice.lower() # Allows user to input capital letters.


if choice_lower == "investment":
    print("You have selected the investment calculator. \n ")  # New line improves code readability.

    # Asks the user for the appropriate inputs. float ensures the user can input decimals.
    deposit = float(input("How much money will you be depositing? "))
    rate = float(input("What is the interest rate? (enter as a number) "))
    time = float(input("How many years do you plan on investing for? "))
    interest = input("Would you prefer simple or compound interest? ").lower()  # .lower() enables the user to input with capitals and for the program to still recognise the input. 

    dec_rate = rate / 100  # Converts interest rate into a decimal to ensure python can calculate the correct amount.

    simple_interest = round(deposit * (1 + dec_rate * time), 2  )  # Calculates interest if simple interest is input by the user rounded to two decimal places.
    compound_interest = round(deposit * math.pow((1 + dec_rate), time), 2)  # Calculates interest if compound interest is input by the user rounded to two decimal places.

    # Prints out the return based on the users inputs and selections. 
    if interest == "simple":
        print(f"\nYou have selected simple interest. This means that if you deposit {deposit} at an interest rate of {rate}% for {time} years it will return £{simple_interest}. ")
    elif interest == "compound":
        print(f"\nYou have selected compound interest This means that if you deposit {deposit} at an interest rate of {rate}% for {time} years it will return £{compound_interest}. ")
    else:
        print("Error. That is not a valid form of interest. ")  # Provides an error message should the user enter an invalid form of interest. 

elif choice_lower == "bond":
    print("You have selected the bond calculator. \n ")  # New line improves code readability.

    # Asks the user for the apprpriate inputs. float ensures the user can enter decimals.
    pv = float(input("What is the present value of the house? "))
    rate = float(input("What is the interest rate? (enter as a number) "))
    months = float(input("How many months do you plan on taking to repay the bond? "))

    dec_rate = rate / 100  # Converts interest rate into a decimal to ensure python can calculate the correct amount.
    i = dec_rate / 12  # Converts dec_interest rate into a monthly rate so it can be applied to the formula.

    repayment = round((i * pv) / (1 - (1 + i) ** (-months)), 2)  # Calculates the payment rounded to two decimal places. 

    print(f"\nWith the current present value of the house at £{pv}, an interest rate of {rate}, and your plan to repay the loan in {months}. The repayment you'll have to pay on your home is £{repayment} each month. ")

else:
    print("Your input is invalid, please input either 'investment' or 'bond'. ")
