current_choice = 10
computer_parts = []
computer_parts_options = [
    'computer', 'monitor', 'keyboard', 'mouse', 'mouse mat',
    'hdmi cable',
]

while current_choice != 0:
    if len(computer_parts_options) >= current_choice > 0:
        if computer_parts_options[current_choice] in computer_parts:
            print(f"Removing {current_choice}")
            computer_parts.remove(computer_parts_options[current_choice])
        else:
            print(f"Adding {current_choice}")
            computer_parts.append(computer_parts_options[current_choice])
    else:
        print("Please add an option from the list below:")
        for number, item in enumerate(computer_parts_options):
            print(f"{number+1}: {item}")
        print("0: to finish")

    current_choice = int(input(f"Please enter you choice from 1 to {len(computer_parts_options)}: "))
print(f"Items added, you have chosen {computer_parts}.")
