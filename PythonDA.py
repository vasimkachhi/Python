import pandas as pd
import warnings
warnings.filterwarnings("ignore")
data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy', 'vasim'],
        'year': [2012, 2012, 2013, 2014, 2014,2016],
        'reports': [4, 24, 31, 2, 3,None],
        'coverage': [25, 94, 57, 62, 70,None]}
df = pd.DataFrame(data, index=['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma', 'Ind'])

df2 = df.copy()


z = pd.merge(df,df2, on=["year",'name', 'reports'], how='inner' )

print z

print df.fillna("")


print df
print df[["year","name"]][1:2]
print df.ix[1:2, 0:3]

a = df.drop_duplicates(subset="year", keep='first')
print a


b = df.dropna(how='any')
print b


#
z = df.groupby(["year"])
for x in z:
    print x[1]

print z

x=  df.loc[df.name.str.contains('m', case=False, na=False)]
x=  df.loc[df.name.str.endswith('a')]
print df[(df.year >2012) & (df.year< 2014)]
x =x.reset_index(drop=False)

print x
print df
print df[::-1]