
account_balance = 0
transaction = []
def bank_account():
    def menu():
        global account_balance
        global details
        print("\n1. Deposit \n2. Withdraw \n3. Check Transaction \n4. Check Account Balance \n5. Exit")
        details = int(input("Enter your choice (The corresponding serial number): "))

        if details == 1 :
            deposit = input("Enter the amount to be deposited:")
            print("Rs." + deposit + " has been deposited")
            a = "Rs." + deposit + " has been deposited"
            transaction.append(a)
            deposit_int = int(deposit)
            account_balance = account_balance + deposit_int


        if details == 2 :
            withdraw = input("Enter the amount you would like to withdraw:")
            withdraw_int = int(withdraw)
            if withdraw_int > account_balance:
                print("Error. Withdraw amount greater than account balance. \nCannot withdraw")
                c = "Failed to withdraw Rs." + withdraw
                transaction.append(c)

            else:
                print("Rs." + withdraw + " has been withdrawn")
                b = "Rs." + withdraw + " has been withdrawn"
                transaction.append(b)
                account_balance = account_balance - withdraw_int


        if details == 3:
            if len(transaction) == 0:
                print("No Transaction History ")
            else:
                print(transaction)

        if details == 4:
            account_bal = str(account_balance)
            print("Bank Balance is " + account_bal)

        if details == 5:
            exit()
    menu()
    options = int(input("For Menu enter 1 \nTo exit type enter 2 \n"))
    #print(type(options)
    if options == 1:
        bank_account()
    else:
        exit()

# Getting input from the user

username = input("Enter username: ")
age = input("Enter age: ")
x = int(age)
if x < 18:
    print("The user is minor.")
    print("Cannot create an account")
    exit()
else:
    print("Eligible to create an account")
print("Do you want to create an account?")
#print("yes or no?")
account = input("yes or no? ")
if account == "yes":
    bank_account()
else:
    exit()
