# 1. Make pi
# just write a function that returns the first 3 digits
# of Pi in a list.
# Pi = 3.14

# input: none
# output: [3, 1, 4]
def make_pi():
    return [3, 1, 4]


# 2. Common End
# write a function that takes two arrays as input
# a. return true if both arrays have THE SAME 1st element
# b. return true if both arrays have THE SAME last element
# c. return false otherwise

# input: a list 'a', and a list 'b'
# output: true or false
def common_end(a, b):
    a_max = len(a) - 1
    b_max = len(b) - 1

    if a[0] == b[0]:
        return True
    elif a[a_max] == b[b_max]:
        return True
    else:
        return False


# Write a function that takes in a string of letters
# called 'letters' and count the total number of each
# letter in the string.
# the output should be a 'dict'

# example: letter_counter("aaaabbcc") -> { 'a': 4, 'b': 2, 'c': 2 }
def letter_counter(letters):
    total = {}
    for letter in letters:
        if total.get(letter):
            total[letter] += 1
        else:
            total[letter] = 1
    return total

# pi = make_pi()
# ans1 = common_end([1, 2, 3], [4, 5, 6])
# ans2 = common_end([1, 2, 3], [4, 5, 3])
# ans3 = common_end([1, 2, 3], [1, 5, 6])
# letter_counts = letter_counter("aaaabbcc")

# print(f'(answer) pi: [3, 1, 4], ans1: False, ans2: True, ans3: True')
# print(f'(your output) pi: {pi}, ans1: {ans1}, ans2: {ans2}, ans3: {ans3}')
# print(letter_counts)

# Calculate GPA
# given a dict of classes and their grade
# return the average of all the grades

# len = get length of container
# def calculate_gpa(grades):
#     total = 0
#     for grade in grades.values():
#         total = total + grade
#     return total / len(grades) # -> give us the average
# grades_1 = {  'Science': 80, 'English': 70,'Math': 80, 'History': 78 }


def calculate_gpa(grades):
    return 0


grades = { 
    'Science': [80, 70, 88, 90], 
    'English': [70, 79, 62, 90, 92], 
    'Math': [80, 82, 81, 90, 90], 
    'History': [78, 84, 96, 100] 
}

gpa = calculate_gpa(grades)

for subject, subject_grades in grades.items():
    print('subject:', subject)
    for i, grade in enumerate(subject_grades):
        print(f'grade {i + 1}: {grade}%')

print('GPA:', gpa)