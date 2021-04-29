#import pandas as pd
FD=pd.read_csv("nobel_final.csv")
FD
FD.head()
FD.tail()
FD["firstname"].head()
FD["firstname"].tail()
type(FD)
len(FD)
FD.shape
FD.info()
FD.describe()