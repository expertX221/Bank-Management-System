import os

# File to store account details
FILE_NAME = "accounts.txt"

# Function to create a new account
def create_account():
    print("\n--- Create New Account ---")
    acc_no = input("Enter Account Number: ")
    name = input("Enter Account Holder Name: ")
    balance = input("Enter Initial Deposit Amount: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{acc_no},{name},{balance}\n")

    print("Account created successfully!\n")


# Function to find an account
def find_account(acc_no):
    if not os.path.exists(FILE_NAME):
        return None

    with open(FILE_NAME, "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == acc_no:
                return data
    return None


# Function to update account details in file
def update_account(acc_no, new_balance):
    lines = []
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    with open(FILE_NAME, "w") as file:
        for line in lines:
            data = line.strip().split(",")
            if data[0] == acc_no:
                data[2] = str(new_balance)
                line = ",".join(data) + "\n"
            file.write(line)


# Deposit money
def deposit():
    print("\n--- Deposit Money ---")
    acc_no = input("Enter Account Number: ")
    account = find_account(acc_no)

    if account:
        amount = float(input("Enter Deposit Amount: "))
        new_balance = float(account[2]) + amount
        update_account(acc_no, new_balance)
        print("Amount deposited successfully!")
    else:
        print("Account not found!\n")


# Withdraw money
def withdraw():
    print("\n--- Withdraw Money ---")
    acc_no = input("Enter Account Number: ")
    account = find_account(acc_no)

    if account:
        amount = float(input("Enter Withdrawal Amount: "))
        balance = float(account[2])
        if amount <= balance:
            new_balance = balance - amount
            update_account(acc_no, new_balance)
            print("Amount withdrawn successfully!")
        else:
            print("Insufficient balance!")
    else:
        print("Account not found!\n")


# Check balance
def check_balance():
    print("\n--- Check Balance ---")
    acc_no = input("Enter Account Number: ")
    account = find_account(acc_no)

    if account:
        print(f"Account Holder: {account[1]}")
        print(f"Current Balance: ₹{account[2]}\n")
    else:
        print("Account not found!\n")


# View account details
def view_account():
    print("\n--- View Account Details ---")
    acc_no = input("Enter Account Number: ")
    account = find_account(acc_no)

    if account:
        print(f"Account Number: {account[0]}")
        print(f"Account Holder: {account[1]}")
        print(f"Balance: ₹{account[2]}\n")
    else:
        print("Account not found!\n")


# Main menu
def main():
    while True:
        print("===== BANK MANAGEMENT SYSTEM =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. View Account Details")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            view_account()
        elif choice == "6":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice! Please try again.\n")


# Run the program
main()
