from person import Person
from bank_account import BankAccount
def person_data():
    name = input("Enter the person's name:\n")
    new_person = Person(name)
    done = "no"
    while done.lower() != "yes":
        acc_num = int(input("Enter a 4-digit account number:\n"))
        initial_balance = float(input("Enter the initial balance:\n"))
        new_account = BankAccount(acc_num, initial_balance)
        new_person.add_account(new_account)
        done = input("Are you done adding accounts? (yes/no):\n")
    return new_person
def balance_summary(person_list):
    for person in person_list:
        total_balance = 0.0
        for account in person.accounts:
            total_balance += account.balance
        print(f"{person.name} : {total_balance:.2f}")
