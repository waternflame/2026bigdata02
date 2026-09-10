import numpy as np
import pandas as pd

df1 = pd.read_csv("./bike.csv")
#print(df1.info())
#print(df1.select_dtypes(include="float")) float 데이터 값만 출력
#print(df1.select_dtypes(exclude="float")) float 데이터 값을 제외하고 출력
#print(df1.filter(regex="d..y"))
#print(df1.filter(items=['windspeed', 'season']))
df2 = df1.set_index('datetime')
#print(df2)
print(df2.filter(like='00:00:00', axis=0))