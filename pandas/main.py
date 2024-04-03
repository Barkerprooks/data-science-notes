# example code:
import pandas as pd

grades = [] # store grades in a list

# ask the user 5 times
for i in range(5):
    grade = input("enter a grade: ")
    grades.append(int(grade))

df = pd.DataFrame(grades)

print(df.mean())
print(df.median())
print(df.mode())