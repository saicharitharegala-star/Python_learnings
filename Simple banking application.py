
balance = 0.0
kyc_docs = {}
def check_balance():
    print("====================================")
    print(f"Your current balance is: {balance}$")
    print("====================================")


def deposit():
    global balance
    deposit_amount = float(input("Enter the amount you want to deposit: "))
    if deposit_amount > 0:
     balance += deposit_amount
     print("===================================================================================")
     print(f"You have successfully deposited {deposit_amount}$. Your new balance is: {balance}$")
     print("===================================================================================")
    else:
        print("Invalid deposit amount! Please enter a positive value.")


def withdraw():
    global balance
    withdraw_amount = float(input("Enter the amount you want to withdraw: "))
    if withdraw_amount > balance :
        print("Insuffieceint funds! You cannot withdraw more than your current balance.")
    elif withdraw_amount <= 0:
        print("Invalid withdraw amount! Please enter a positive value.")
    else:
        balance -= withdraw_amount
        print("====================================================================================")
        print(f"You have successfully withdrawn {withdraw_amount}$. Your new balance is: {balance}$")
        print("====================================================================================")
def update_kyc(**docs):
    global kyc_docs 
    kyc_docs.update(docs)
def check_kyc():
    if kyc_docs:
        print("====================================")
        print("KYC Documents:")
        for key, value in kyc_docs.items():
            print(f"{key}: {value}")
        print("====================================")
    else:
        print("No KYC documents found. Please update your KYC information.")
if __name__ == "__main__":
    while True:
        print("===========================================")
        print("Welcome to the Simple Banking Application!")
        print("===========================================")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Update KYC")
        print("5. Check KYC")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            check_balance()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            docs = {}
            n_documents = int(input("Please provide your KYC information(number of documents to be submitted):"))
            for i in range(n_documents):
                key = input("Enter document type: ")
                value = input("Enter document number: ")
                docs[key] = value
            update_kyc(**docs)
            print("=====================================")
            print("KYC information updated successfully!")
            print("=====================================")
        elif choice == '5':
            check_kyc()
        elif choice == '6':
            print("Thank you for using the Simple Banking Application. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

