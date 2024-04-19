import random
import pandas as pd
import matplotlib.pyplot as plt

delays = pd.read_csv('pandas/airline.csv')
coordinates = pd.read_csv("pandas/coordinates.csv")

print('part 1: loaded CSV file, # of rows:', len(delays.index))

f1 = delays['airport_name'].str.contains('TX')
f2 = delays['airport_name'].str.contains('TN')

print('part 3: list of Texas and Tennessee:', delays[f1 | f2])

flights = delays + coordinates # merge the datasets

fig, ax = plt.subplots()
x = coordinates['long']
y = coordinates['lat']

print(x)

ax.scatter(x, y)
plt.show()