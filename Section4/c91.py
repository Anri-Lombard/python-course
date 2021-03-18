current_choice = input("Please enter you choice from 1 to 5: ")
computer_parts = []

while current_choice != "0":
    if current_choice in "12345":
        print(f"Adding {current_choice}")
        if current_choice == "1":
            computer_parts.append("computer")
        elif current_choice == "2":
            computer_parts.append("monitor")
        elif current_choice == "3":
            computer_parts.append("keyboard")
        elif current_choice == "4":
            computer_parts.append("mouse")
        elif current_choice == "5":
            computer_parts.append("mouse mat")
        else:
            print("This is an invalid choice")
    else:
        print("Please add an option from the list below:")
        print("1: computer")
        print("2: monitor")
        print("3: keyboard")
        print("4: mouse")
        print("5: mouse mat")
        print("0: to finish")
print(f"Items added, you have chosen {computer_parts}")
