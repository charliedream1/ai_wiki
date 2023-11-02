import pandas as pd

df = pd.read_csv(r'C:\Users\Administrator\Downloads\combine.csv')
# 逐行扫描，任一一列有空值的行就剔除掉
df = df.dropna(axis=0, how='any')
df.to_csv(r'C:\Users\Administrator\Downloads\combine_new.csv')
pass
