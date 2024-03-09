import pandas as pd

df = pd.read_csv("diabetes.csv")
rows, cols = df.shape

xs = [1, 2, 3, 4, 5, 6, 7]
first3 = xs[:3]
last3 = xs[3:]
mid3 = xs[2:5]

