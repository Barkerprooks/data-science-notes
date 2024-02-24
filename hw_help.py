def letter_count(letters):
    counts = {} # we need this to keep track of each letter
    for letter in letters: # go through each letter
        if counts.get(letter): # the letter exists in the dict
            counts[letter] += 1 # we found a letter, add 1 to the total
        else: # we did not find the letter, so we need to add it
            counts[letter] = 1 # we have found one so far
    return counts # pass it back as output


if __name__ == "__main__":

    # counts = letter_count("abba")

    # for letter, count in counts.items():
    #     print(letter, count)

    running = True

    while running:
        user_input = input('command (1 = say hello, 2 = quit): ')
        if user_input == "1":
            print('hello')
        if user_input == "2":
            running = False