import random

# Ask user if they want to play lotto
choice = input("Did you want to play lotto? (yes/no): ")
if choice == "yes":
    max_49 = input("Press 1 for 6/49 or 2 for Lotto Max: ")
    if max_49 == "1":
        print("You choose 6/49")
        lotto_49 = random.sample(range(1, 50), 6)
        print(lotto_49)
    elif max_49 == "2":
        print("You choose Lotto Max")
        lotto_max = random.sample(range(1, 50), 7)
        print(lotto_max)
    else:
        print("You choose wrong number")
else: 
    "You choose not to play lotto"
