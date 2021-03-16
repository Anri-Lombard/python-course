shopping_list = "milk pasta eggs spam bread rice".split()

for item in shopping_list:
    if item == 'spam':
        continue
    print(f"Buy {item}")