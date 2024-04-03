numbers = []

for i in range(3):
    user_input = input('input number: ')
    number = float(user_input)
    numbers.append(number)

for number in numbers:
    print(number * 2)