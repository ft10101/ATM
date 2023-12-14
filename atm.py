print("\nWelcome to ATM\n")
PIN = 1211
print("Your ATM Pin is:", PIN)
balance = 1000
print("\n\nEnter the 4 digit pin: ")
pin = input()
if pin == PIN:
    print("\nThank you for banking with us!\n")
    print("\nYour current balance is: ", balance,"\n")
    while True:
        print("\n\nPlease choose among the following services:\n")
        print("1 - CASH WITHDRAWAL\n")
        print("2 - FUND TRANSFER\n")
        print("3 - CASH DEPOSIT\n")
        print("4 - BALANCE INQUIRY\n")
        print("5 - EXIT\n")
        x = int(input())  
        if x == 1:
            print("Enter the amount you want to withdraw:")
            withdraw_amount = int(input())
            if withdraw_amount > balance:
                print("\nInsufficient balance\n\nTry again..\nYour current balance is: ", balance)
                continue
            else:
                print(withdraw_amount," is withdrawn from your account\n")
                balance -= withdraw_amount
                print("\nYour account balance is: ", balance)
            print("Continue banking with us?\nPress y to continue and n to exit:")
            yes_no = input()
            if yes_no == 'y' or yes_no == 'Y':
                continue
            else:
                break
        elif x == 2:
            print("Enter the account number:")
            account_no = int(input())
            print("\n\nEnter the amount you want to transfer to ", account_no)
            transfer_amount = int(input())
            if transfer_amount > balance:
                print("\nInsufficient balance\n\nTry again..\nYour current balance is: ", balance)
                continue
            else:
                print("\n\n",transfer_amount,"rupees is transfered to ",account_no)
                balance -= transfer_amount
                print("\nYour account balance is: ", balance)
            print("\n\nContinue banking with us?\nPress y to continue and n to exit: ")
            yes_no = input()
            if yes_no == 'y' or yes_no == 'Y':
                continue
            else:
                break
        elif x == 3:
            print("Enter the amount you want to deposit: ")
            deposit_amount = int(input())
            balance += deposit_amount
            print("\n\n",deposit_amount,"rupees is deposited into your account\n")
            print("\nYour current balance is: ", balance)
            print("\n\nContinue banking with us?\nPress y to continue and n to exit: ")
            yes_no = input()
            if yes_no == 'y' or 'Y':
                continue
            else:
                break
        elif x == 4:
            print("\n\nYour account balance is: ", balance)
            continue
        elif x == 5:
            break
        else:
            print("\n\nInvalid choice.. \nTry again\n")
            continue
else:
    print("Incorrect PIN.\nTry again..")
