numbers = input("Plese enter a series of numbers, using any seperators you like: ")
separators = ""

for char in numbers:
    if not char.isnumeric():
        separators += char

values = "".join(char if char not in separators else " " for char in numbers).split()
print(sum([int(val) for val in values]))
