import random

# Ask user if they want to play lotto
choice = input("Did you want to play lotto? (yes/no): ")

i = choice.lower()

while i == "yes" and i != "no":
    max_49 = input("Press 1 for 6/49 or 2 for Lotto Max and 3 for exit: ")
    if max_49 == "1":
        print("You choose 6/49")
        lotto_49 = random.sample(range(1, 50), 6)
        print(lotto_49)
    elif max_49 == "2":
        print("You choose Lotto Max")
        lotto_max = random.sample(range(1, 50), 7)
        print(lotto_max)
    elif max_49 == "3":
        i = "no"
    else:
        print("You choose wrong number")
else: 
    print("Thanks for using this application!")
