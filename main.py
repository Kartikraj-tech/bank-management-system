def showBalance():
    print(f" your current balance is ${balance}")
def deposit():
    amount = int(input("enter the amount : "))
    if (amount <=0):
        print("invalid amount")
        return 0
    else:
        return amount
def withdraw():
    amount = int(input("enter the amount : "))
    if (amount > balance):
        print(" insufficient funds")
        return 0
    else:
        return amount

balance = 0
running = True

print("Bank Management System")
print("Press 1 to show balance")
print("Press 2 to deposit")
print("Press 3 to withdraw")
print("Press 4 to exit")

while running:
    choice = int(input("enter your choice : "))
    if (choice == 1):
        showBalance()
    elif(choice == 2):
        balance += deposit()
    elif(choice == 3):
        balance -= withdraw()
    elif(choice == 4):
        running = False
    else:
        print("Invalid choice ")
        running = False

print("Thank you ! for using our banking service 🤗")