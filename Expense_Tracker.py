# Author: Dhruv
expenses = []

while True:

    print("\n----------")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. Show total spent")
    print("4. exit")

    usernumber = input("Enter a number from (1-4) :")

    if usernumber == "1":
        amount = int(input("Plese enter your expense amount :"))
        reason = input("Plese enter your reason :")

        expense = (amount , reason)
        expenses.append(expense)

    elif usernumber == "2":

        if not expenses:
            print("\n-----SOMETHING WENT WRONG-----")
            print("No expense(s) available.")

        else:
            print("\n-----YOUR EXPENSES ARE-----")

            for i, task in enumerate(expenses, 1):  #enumerate used to check index number and item
                print(f"{i}. {task}")    #Here we start form 1 that why its shows index 1 insted 0

    elif usernumber == "3":

        if not expenses:
            print("\n-----SOMETHING WENT WRONG-----")
            print("No expense(s) available.")

        else:
            total = 0
            for expense in expenses:
                amount, reason = expense
                total = total + amount
                
            print("\nYour total expense(s) are")
            print(total)

    elif usernumber == "4":
        print("Control your expenses with us")
        print("Good bye...")

        break

    else:
        print("Invalid choice")
