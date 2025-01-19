class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the bank account with an optional initial balance.
        :param initial_balance: Initial amount in the account (default is 0).
        """
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit the specified amount into the account.
        :param amount: Amount to deposit (must be positive).
        """
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw the specified amount from the account if funds are sufficient.
        :param amount: Amount to withdraw.
        :return: True if withdrawal is successful, False otherwise.
        """
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Print the current account balance.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")

# main-0.py
import sys
from bank_account import BankAccount

def main():
    """
    Main function to handle command-line interactions with the BankAccount class.
    """
    account = BankAccount(100)  # Example starting balance

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse command and amount from arguments
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
