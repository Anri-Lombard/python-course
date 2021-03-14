name = input("What is you name? ")
age = int(input("What is your age? "))

if 18 < age < 31:
    print(f"Welcome {name}! We hope this adventure will leave memories you won't ever forget!")
elif 18 > age:
    print(f"Sorry {name}, rather come back in {18 - age} years.")
elif age > 31:
    print(f"Age is wisdom {name}. It will be wise to stay away from this adventure I advise.")
