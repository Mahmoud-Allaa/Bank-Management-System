from time import sleep

customers = [
    {
        'name': "Mahmoud Alaa",
        'phone': '010',
        'email': '1',
        'password': '1',
        'balance': 0
    },
    {
        'name': "Mahmoud Alaa",
        'phone': '010',
        'email': 'mahmoud@alaa.com',
        'password': '000',
        'balance': 0
    },

    {
        'name': 'Sayed Alaa',
        'phone': '011',
        'email': 'sayed@alaa.com',
        'password': '000',
        'balance': 0
    },

    {
        'name': "Salah Alaa",
        'phone': '012',
        'email': 'salah@alaa.com',
        'password': '000',
        'balance': 0
    },
]


def print_pause(message):
    print(message)
    sleep(1)  # Add a delay of 1 second between messages


def get_valid_input(choices, msg):
    choice = input(msg).strip()
    while choice not in choices:
        print_pause("Invalid input. Please try again.")
        choice = input(msg).strip()
    print("")
    return choice


def sign_up():
    name = input("Enter Your Name: ")
    phone = input("Enter Your Phone: ")
    email = input("Enter Your E-mail: ")
    password = input("Enter Your Password: ")
    new_customer = {
        'name': name,
        'phone': phone,
        'email': email,
        'password': password,
        'balance': 0
    }

    if not (name and phone and email and password) == '':
        customers.append(new_customer)
        print(f'\nWelcome {new_customer["name"]}\n')
        return new_customer


def sign_in():
    email = input("Enter Your E-mail: ")
    password = input("Enter Your Password: ")

    for customer in customers:
        if customer["email"] == email and customer["password"] == password:
            print_pause(f'\nWelcome {customer["name"]}\n')
            return customer

    print_pause('\nE-mail or Password is Wrong! :(\n...')
    sign_in()


def logout():
    print_pause('Logging out ...')
    sleep(2)
    print_pause('\nLoged out')


def view_account_details(customer):
    print_pause(f'Name is:    {customer["name"]}')
    print_pause(f'Phone is:   {customer["phone"]}')
    print_pause(f'E-mail is:  {customer["email"]}')
    print_pause(f'Balance is: {customer["balance"]}')


def deposit_amount(customer):  # قيمةالايداع
    print_pause(f'You have {customer["balance"]} Egyption Pound')
    while True:
        amount = input('\nHow much you want to deposit: ').strip()
        if amount.isdigit():
            customer["balance"] += int(amount)
            print_pause("\nSuccessful Operation :)")
            print_pause(
                f'\nNow You have {customer["balance"]} Egyption Pound')

            return customer
        else:
            print_pause("Only Numbers you can enter")


def withdraw_amount(customer):  # قيمةالسحب
    print_pause(f'You have {customer["balance"]} Egyption Pound')
    while True:
        amount = input('\nHow much you want to withdraw: ').strip()
        if amount.isdigit() and not int(amount) > customer["balance"]:
            print_pause("Successful Operation :)")
            customer["balance"] -= int(amount)
            print_pause(
                f'\nNow You have {customer["balance"]} Egyption Pound')
            return customer
        elif amount.isdigit() and int(amount) > customer["balance"]:
            print_pause("denied Operation :(")
            print_pause("The current amount less then you want!")
            return customer
        else:
            print_pause("Only Numbers you can enter :(")
