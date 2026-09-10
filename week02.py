import numpy as np
import pandas as pd

df1 = pd.read_csv("./bike.csv")
#print(df1.head())
#print(df1.info())
#print(df1['temp'])
print(df1.loc[df1['season'] != 1])
#print(df1.iloc[3:8,3:7]) #3열부터 8열까지, 3행부터 6행까지 출력
#print(df1.loc[3:7,'workingday':'atemp']