import pandas as pd

df = pd.read_csv('data.csv')
summary = df.describe()
print(summary)
