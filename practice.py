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


# def calculate_gpa(grades):

#     number_of_grades = 0
#     total_grades = 0

#     for subject_grades in grades.values():
#         number_of_grades += len(subject_grades)
#         total_grades += sum(subject_grades)
    
#     return total_grades / number_of_grades


# grades = { 
#     'Science': [80, 70, 88, 90], 
#     'English': [70, 79, 62, 90, 92], 
#     'Math': [80, 82, 81, 90, 90],
#     'History': [78, 84, 96, 100] 
# }

# gpa = calculate_gpa(grades)

# for subject, subject_grades in grades.items():
#     print('subject:', subject)
#     for i, grade in enumerate(subject_grades):
#         print(f'grade {i + 1}: {grade}%')

# print('GPA:', gpa)


salaries = [
    {"name": "bob", "salary": 60000, "title": "IT"},
    {"name": "joe", "salary": 70000, "title": 'HR'},
    {"name": "sally", "salary": 90000, "title": "Developer"},
    {"name": "jim", "salary": 78000, "title": 'HR'},
    {"name": "bart", "salary": 30000, "title": 'HR'},
    {"name": "sarah", "salary": 60030, "title": "IT"},
    {"name": "frank", "salary": 90400, "title": "Developer"},
]


def find_highest_paid_employee(salaries):
    highest_salary = 0
    highest_name = "no one"
    for employee in salaries:
        if employee["salary"] > highest_salary:
            highest_salary = employee["salary"]
            highest_name = employee["name"]
    return highest_name


def find_lowest_paid_employee(salaries):
    lowest_salary = 1e99
    lowest_name = "no one"
    for employee in salaries:
        if employee["salary"] < lowest_salary:
            lowest_salary = employee["salary"]
            lowest_name = employee["name"]
    return lowest_name



def get_total_salaries(salaries):
    total_salaries = {}
    for employee in salaries:
        title = employee["title"]
        salary = employee["salary"]
        if total_salaries.get(title):
            total_salaries[title].append(salary)
        else:
            total_salaries[title] = [ salary ]
    return total_salaries


def find_highest_paid_title(salaries):
    highest_avg_salary = 0
    highest_avg_title = "no one"
    
    for title, title_salaries in get_total_salaries(salaries).items():
        avg_salary = sum(title_salaries) / len(title_salaries)
        if highest_avg_salary < avg_salary:
            highest_avg_salary = avg_salary
            highest_avg_title = title

    return highest_avg_title, highest_avg_salary


def find_lowest_paid_title(salaries):
    lowest_avg_salary = 1e99
    lowest_avg_title = "no one"
    
    for title, title_salaries in get_total_salaries(salaries).items():
        avg_salary = sum(title_salaries) / len(title_salaries)
        if lowest_avg_salary > avg_salary:
            lowest_avg_salary = avg_salary
            lowest_avg_title = title

    return lowest_avg_title, lowest_avg_salary


# print("Employee Report")
# print("Highest paid title:", find_highest_paid_title(salaries))
# print("Lowest paid title:", find_lowest_paid_title(salaries))
# print("Highest paid:", find_highest_paid_employee(salaries))
# print("Lowest paid:", find_lowest_paid_employee(salaries))





# Return the "centered" average of an array of ints, which we'll say 
# is the mean average of the values, except ignoring the largest and 
# smallest values in the array. If there are multiple copies of the
# smallest value, ignore just one copy, and likewise for the largest 
# value. Use int division to produce the final average. You may assume that the array is length 3 or more.
def centered_average(numbers):
    centered_numbers = []
    smallest = min(numbers)
    biggest = max(numbers)

    for number in numbers:
        if smallest == number:
            continue
        if biggest == number:
            continue
        centered_numbers.append(numbers)

    return sum(centered_numbers) / len(centered_numbers)



class DataRow:
    def __init__(self, name, salary, title):
        self.name = name
        self.salary = salary
        self.title = title

    def __str__(self):
        return f'name: {self.name}, salary: {self.salary}, job title: {self.title}'
    
d = {"name": "bob", "salary": 60000, "title": "IT"}
print(d["name"])

r = DataRow("bob", 60000, "IT")
print(r.name)

salaries = [
    DataRow("bob", 60000, "IT"),
    DataRow("joe", 70000, 'HR'),
    DataRow("sally", 90000, "Developer"),
    DataRow("jim", 78000, 'HR'),
    DataRow("bart", 30000, 'HR'),
    DataRow("sarah", 60030, "IT"),
    DataRow("frank", 90400, "Developer"),
]

def find_highest_paid_employee(salaries):
    highest_salary = 0
    highest_name = "no one"
    for employee in salaries:
        if employee.salary > highest_salary:
            highest_salary = employee.salary
            highest_name = employee.name
    return highest_name

def find_smallest_paid_employee(salaries):
    smallest_found = salaries[0]
    for employee in salaries:
        if employee.salary < smallest_found.salary:
            smallest_found = employee
    return smallest_found


def get_total_salaries(salaries):
    total_salaries = {}
    for employee in salaries:
        title = employee.title
        salary = employee.salary
        if total_salaries.get(title):
            total_salaries[title].append(salary)
        else:
            total_salaries[title] = [ salary ]
    return total_salaries


def find_highest_paid_title(salaries):
    highest_avg_salary = 0
    highest_avg_title = "no one"
    
    for title, title_salaries in get_total_salaries(salaries).items():
        avg_salary = sum(title_salaries) / len(title_salaries)
        if highest_avg_salary < avg_salary:
            highest_avg_salary = avg_salary
            highest_avg_title = title

    return highest_avg_title, highest_avg_salary
