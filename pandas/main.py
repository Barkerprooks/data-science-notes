import pandas as pd

# series = pd.Series([1, 2, 3, 4, 5])
# new_series = series.apply(lambda x: x * 2)

# names = {'name': ['Jon Doe', 'Jane Doe', 'Mickey Mouse'],
#               'age' : [22, 25, 24],
#               'occ' : ['software engineer', 'Data Scientist', 'Clown']}

# salary = {'money': [100, 200, 300],
#          'name': ['Jon Doe', 'Jane Doe', 'Mickey Mouse']}

# df1 = pd.DataFrame(names)
# df2 = pd.DataFrame(salary)

# merged = pd.merge(df1, df2, how='inner', on='name')

# print(merged.describe())


# 1. Read airline.csv into the program as a Pandas DataFrame
# path: "pandas/airline.csv"
table = pd.read_csv("pandas/airline.csv")

# 2. Display all Texas and Tennessee airports
texas_rows = table.airport_name.str.contains('TX')
tennessee_rows = table.airport_name.str.contains('TN')
rows = table.loc[tennessee_rows | texas_rows]['airport_name']
print(rows)

# 3. Display how many arrivals into JFK in 2019 encountered both weather and carrier delays.
jfk = table.airport == "JFK"
year = table.year == 2019
weather = table.weather_delay > 0
carrier = table.carrier_delay > 0

rows = table.loc[jfk & year & weather & carrier]
print(rows)