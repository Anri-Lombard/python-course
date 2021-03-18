import random

count = 0
still_playing = True
guess = 0
high = 1000
low = 1
answer = random.randint(low, high)

while guess != answer:
    print(f"Please guess a number between {low} and {high}: ")
    guess = int(input())
    count += 1
    if guess == answer and count == 1:
        print("You got it the first time!")
        still_playing = False
    else:
        if guess == answer:
            print(f"Correct! You took {count} tries.")
        elif guess < answer:
            print("Too low, please guess higher: ")
            low = guess
            continue
        else:
            print("Too high, please guess lower: ")
            high = guess
            continue

print("Feel free to try Again.")
