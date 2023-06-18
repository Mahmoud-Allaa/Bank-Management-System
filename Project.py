from utils import *


def main():
    current_customer = {}
    signup_or_signin = get_valid_input(
        ['1', '2'], "To sign up enter 1, To sign in enter 2: ")

    if signup_or_signin == '1':
        current_customer = sign_up()

    elif signup_or_signin == '2':
        current_customer = sign_in()

    while True:
        print_pause(
            "What you want to do? (View account details / Deposit amount / Withdraw amount / Logout)\n...")
        operation = get_valid_input(
            ['1', '2', '3', '4'], "Enter 1 to View account details, 2 to Deposit amount, 3 to Withdraw amount, 4 to Logout: ")

        if operation == '1':
            view_account_details(current_customer)

        elif operation == '2':
            current_customer = deposit_amount(current_customer)

        elif operation == '3':
            withdraw_amount(current_customer)

        elif operation == '4':
            logout()
            break

        print_pause('\n...')
        another_operation = get_valid_input(
            ['y', 'n'], "Would you do another operation? (Y/N)")
        if another_operation == 'n':
            break

    # Playing again
    choice = input("Play again? (Y/N): ")
    if choice == 'y':
        main()
    else:
        print_pause("Thanks for playing :)")


main()
