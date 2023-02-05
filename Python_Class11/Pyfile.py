import pandas as pd



# Belgium     Brussels        11190846
# India       New Delhi       1303171035
# Brazil      Brasilia        207847528


# Country     Belgium     India       Brazil
# Capital     Brussels    New Delhi   Brasilia
# Population  11190846    1303171035  207847528


data = {'Country': ['Belgium',  'India',  'Brazil'],

'Capital': ['Brussels',  'New Delhi',  'Brasilia'],

'Population': [11190846, 1303171035, 207847528]} 

df = pd.DataFrame(data,columns=['Country',  'Capital',  'Population'])


pd.read_csv('file.csv', header=None, nrows=5)

df.to_csv('myDataFrame.csv')



xlsx = pd.ExcelFile('file.xls')

df = pd.read_excel(xlsx,  'Sheet1')


df.drop('Country', axis=1) 

df.sort_values(by='Country')

df.shape

df.index

df.columns

df.mean()

df.median()

new_df = df.head(5).copy()

df.drop_duplicates()

