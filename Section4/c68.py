import random

answer = random.randint(1, 10)
count = 0
still_playing = True
guess = 0
high = 10
low = 1

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

print("Game Over! Try Again.")
