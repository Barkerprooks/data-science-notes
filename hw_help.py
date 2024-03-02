phonebook = {}
user_input = ''

while user_input != "3":
    user_input = input("command (1 search, 2 add, 3 quit): ")
    
    if user_input == "1":
        name = input('name: ')
        number = phonebook.get(name)
        if number:
            print(number)
        else:
            print("no name exists")
    elif user_input == "2":
        name = input('name: ')
        phonebook[name] = input('number: ')
        print("saved " + name + "'s number")