import pandas as pd


df = pd.read_csv('vehicles.csv')
df.insa().sum()

print(df)