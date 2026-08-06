import pandas as pd
import csv

# data = {"name": ["Andy", "Binh"], "age": [25, 30]}
# df = pd.DataFrame(data)
# print(df)
# print(df.columns)
# print(df.shape)

df = pd.read_csv("D:/AndyProject/AndyFundamental/Day4/people.csv")

# print(df.loc['Andy'])
# print(df.iloc[0])            
# print(df[df['age'] > 27])

df['is_adult'] = df['age'] >= 18 

print(df)


print(df['age'].mean())
print(df['age'].max())
print(df['age'].min())
print(df['age'].sum())
# big_df = pd.DataFrame({"n": range(100)})
# print(big_df)        # compare this...
# print(big_df.head()) # ...to this

# print(df.dtypes)

print(df.groupby('city')['age'].mean())