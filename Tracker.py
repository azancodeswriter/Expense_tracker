import os 

print("             WELLCOME TO EXPENSE TRACKER         ")
print()
print("          Add | View | Total | Search | Exit        ")
print()
options = input("              Choose an option : ")
print()
if options.lower() == "add":
    date = input(" Enter date (dd-mm-yyyy) : ")
    count = input(" How many task you want to add for this date : ")
    for n in count:
        catg = input(" Enter category (e.g., food, transport) : ")
        amount = input(" Enter amount : ")
        desc = input(" Enter description : ")
        with open("data.txt", "a") as f:
            f.write(f"{date} | {catg} | {amount} | {desc}\n")

elif options.lower() == "view": 
    print("              All Task | Specific Task              ") 
    print()
    view = input(" Choose an option : ")
    view.replace(" ","") 
    if view.lower() == "alltask":
        with open("data.txt", "r") as file:
            task = file.read()
            print(task)
    elif view.lower() == "specifictask":
        task = input(" Enter the date for the tasks : ")
        with open("data.txt", "r") as file:
            dat = file.read()
            for tasks in task:
                if dat == task(date):
                    print(task)
                else:
                    print("           No data found          ")
    else:
        print("           INVALID INPUT         ") 

elif options.lower() == "total":
    with open ("data.txt" , "r") as f:
        moneys = f.read(amount)
        spending = 0
        for money in moneys:
            spending += money
            print(f"        Here is the total spendings : {spending}       ")

elif options.lower() == "search":
    catg1 = input(" Enter category (e.g., food, transport) : ")
    print()
    
    with open ("data.txt" , "r") as f:
        reads = f.read()
        for read in reads:
            if catg1 == read(catg):
                print(read)
            else:
                print("           No data found          ")

elif options.lower() == "exit":
    print("            Thanks for using            ")

else:
    print("           INVALID INPUT         ")                       




import os

print("             WELCOME TO EXPENSE TRACKER         ")
print()
print("          Add | View | Total | Search | Exit        ")
print()
options = input("              Choose an option : ")
print()

if options.lower() == "add":
    date = input(" Enter date (dd-mm-yyyy): ")
    count = int(input(" How many tasks you want to add for this date: "))
    for _ in range(count):
        catg = input(" Enter category (e.g., food, transport): ")
        amount = input(" Enter amount: ")
        desc = input(" Enter description: ")
        with open("data.txt", "a") as f:
            f.write(f"{date} | {catg} | {amount} | {desc}\n")
    print(" All tasks added successfully.")

elif options.lower() == "view":
    print("              All Task | Specific Task              ") 
    print()
    view = input(" Choose an option: ").replace(" ", "").lower()
    
    if view == "alltask":
        with open("data.txt", "r") as file:
            data = file.read()
            print(data)
    
    elif view == "specifictask":
        task_date = input(" Enter the date for the tasks (dd-mm-yyyy): ")
        with open("data.txt", "r") as file:
            found = False
            for line in file:
                if task_date in line:
                    print(line.strip())
                    found = True
            if not found:
                print(" No data found for that date.")

    else:
        print(" INVALID INPUT") 

elif options.lower() == "total":
    total = 0
    with open("data.txt", "r") as f:
        for line in f:
            parts = line.strip().split(" | ")
            if len(parts) >= 3:
                try:
                    total += float(parts[2])
                except:
                    pass
    print(f" Total Spendings: ₹{total}")

elif options.lower() == "search":
    catg1 = input(" Enter category to search (e.g., food, transport): ").lower()
    found = False
    with open("data.txt", "r") as f:
        for line in f:
            if catg1 in line.lower():
                print(line.strip())
                found = True
    if not found:
        print(" No data found for that category.")

elif options.lower() == "exit":
    print(" Thanks for using the Expense Tracker! ")

else:
    print(" INVALID INPUT ")



