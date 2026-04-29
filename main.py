from person import Person
from bank_account import BankAccount
import utils

def main():
    people = []

    while True:
        print("\nChoose an option:")
        print("1. Add a new person")
        print("2. Add an account to a person")
        print("3. Show all balances")
        print("4. Quit")
        
        option = input()

        if option == "1":
            new_p = utils.person_data()
            people.append(new_p)

        elif option == "2":
            search_name = input("Enter the person's name:\n")
            found = False
            for p in people:
                if p.name == search_name:
                    acc_num = int(input("Enter a 4-digit account number:\n"))
                    initial_balance = float(input("Enter the initial balance:\n"))
                    p.add_account(BankAccount(acc_num, initial_balance))
                    found = True
                    break
            if not found:
                print("Person not found.")

        elif option == "3":
            if not people:
                print("No data to show.")
            else:
                utils.balance_summary(people)

        elif option == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    main()