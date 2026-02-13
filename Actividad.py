def show_menu():
    print("Choose one option you want")
    print("1.Record a purchase")
    print("2.Calculate the points obtained")
    print("3.Check points balance")
    print("4.Redeem points")
    print("5.Get out of program")
print("----------------------------------------")

print("\n Welcome to the points system")
client = input("name of client: ")
print("Hello",client,"¿what do you want to do?")

def record_purchase():
    print("\n-------Record purchase--------")

    purchase_name = input("Enter the purchase's name:")
    try:
        purchase_value =float(input("Enter purchase amount:"))
        if purchase_value <= 0:
            print("The value must be greater than zero.")
            return 0
        points_earned = int(purchase_value // 1000)
        print(f"You earned {points_earned} points.")
        return points_earned
    except ValueError:
        print("Invalid value. Please enter a number.")
        return 0
total_points = 0
exit_program = False


while not exit_program:

    show_Menu()
    try:
        election = int(input("Enter the option you want:"))
    except ValueError:
        print("Invalid option")
        continue

    if election == 1:
        points = record_Purchase()
        print("purchase successfully registered")
        total_points += points
    elif election ==2:
        print("Calculateing the points obtained")
    elif election ==3:
        print("Your current points balance is:",total_points)
    elif election ==4:
        print("Redeeming points")
    elif election ==5:
        print("Goodbye! see you soon.")  
        exit_program = True  
    print("----------------------------------------------")
        

