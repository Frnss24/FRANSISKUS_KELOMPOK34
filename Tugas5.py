# BankAccount Class (Using Methods with Non-return and Return Types)
class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0  # Starting balance is 0

    # Non-return type method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Current balance is ${self.balance}.")
        else:
            print("Deposit amount must be greater than zero.")

    # Non-return type method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance is ${self.balance}.")
        else:
            print("Insufficient balance or invalid amount.")

    # Return type method to check balance
    def check_balance(self):
        return f"Account balance for {self.account_holder} is ${self.balance}."


# Function with Return Type (returns user choice)
def choose_option():
    print("\nBanking System Options:")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")
    option = int(input("Enter your choice (1-4): "))
    return option


# Function with Non-return Type (performs the banking operations)
def manage_bank_account():
    account_holder = input("Enter the account holder's name: ")
    account = BankAccount(account_holder)  # Creating a BankAccount object

    while True:  # Loop for continuous operation
        option = choose_option()  # Calling a return-type function to get user input

        # Conditional logic for banking operations
        if option == 1:
            balance = account.check_balance()  # Method with return type
            print(balance)
        elif option == 2:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)  # Non-return type method to deposit
        elif option == 3:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)  # Non-return type method to withdraw
        elif option == 4:
            print("Thank you for banking with us!")
            break  # Exit the loop
        else:
            print("Invalid option. Please try again.")


# Main function to start the banking system
if __name__ == "__main__":
    manage_bank_account()  # Start the banking system
