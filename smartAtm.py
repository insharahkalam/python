account_balance = 20000
correct_pin = 1234
attempts = 3
withdraw_limit = 15000
withdrawn_amount = 0
is_logged_in = False
history = []

# ATM PIN Verification
for attempt in range(attempts):
    entered_pin = int(input("Please enter your PIN: "))

    if entered_pin == correct_pin:
        is_logged_in = True
        print("Welcome! Login Successful.")
        break
    else:
        print("Incorrect PIN. Try Again!")

if not is_logged_in:
    print("Your Account Has Been Blocked!")

else:
    while True:
        print("\n------ ATM MENU ------")
        print("1. Balance Inquiry")
        print("2. Cash Deposit")
        print("3. Cash Withdrawal")
        print("4. View Transactions")
        print("5. Logout")

        option = int(input("Select an option: "))

        if option == 1:
            print("Available Balance:", account_balance)

        elif option == 2:
            amount = int(input("Enter deposit amount: "))

            if amount > 0:
                account_balance += amount
                history.append("Deposited: " + str(amount))
                print("Amount Deposited Successfully!")
                print("Updated Balance:", account_balance)
            else:
                print("Please enter a valid amount.")

        elif option == 3:
            amount = int(input("Enter withdrawal amount: "))

            if amount > 0 and amount <= account_balance and amount <= withdraw_limit:
                account_balance -= amount
                withdrawn_amount += amount
                history.append("Withdrawn: " + str(amount))

                print("Cash Withdrawal Successful!")
                print("Remaining Balance:", account_balance)

            else:
                print("Transaction Failed! Check Balance or Withdrawal Limit.")

        elif option == 4:
            print("\n--- Transaction Records ---")

            if len(history) == 0:
                print("No Transactions Found.")
            else:
                for record in history:
                    print(record)

        elif option == 5:
            print("Thank You for Using Our ATM!")
            break

        else:
            print("Invalid Option! Please Select Again.")