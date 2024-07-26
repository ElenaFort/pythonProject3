import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data)

print()

data['meaning'] = 1
df = data.pivot(columns='whoAmI', values='meaning')
df.columns.name = None
df1 = df.fillna(0)
df2 = df1.astype(int)
print(df2)
