import pandas as pd


ship=pd.read_csv('train.csv')

print(ship.shape)##to display no of row and col


print(ship.isnull())

cleanedship=ship.fillna("00")

print(cleanedship.isnull().sum())

cleanedship.to_csv('cleanedship.csv',index=False)

new1=pd.read_csv('cleanedship.csv')

print(new1.isnull())

for name, dtype in new1.dtypes.iteritems():
    print(name, dtype)