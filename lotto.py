import random

length_input = input("Enter how many numbers you need: ")
length_input = int(length_input)
min_number = 1
max_number = input("Last digit that you can enter: ") 
max_number = int(max_number)
numbers = []

while len(numbers) < length_input:
    num = random.randint(min_number, max_number)
    if num not in numbers:
        numbers.append(num)

print(numbers)
