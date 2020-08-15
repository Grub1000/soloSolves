import numpy as np
import pandas as pd
def header(msg):
    print("[" + msg + "]")

# Hard coding data into a Dataframe below
header("1. load hard coded data into df")
df = pd.DataFrame([["name1", 18, 20], ["name2", 24, 1000], ["name3", 20, 50]], index= [0, 1, 2], columns= ["Names", "age", "Money"])
print(df)

# Reading from text file and turning it into a DataFrame below
filename = '../DataScience/Freemont_Weather.txt'
df = pd.read_csv(filename)
header("2. Read text file into df ")
print(df)

# printing the first 5 or last 3 rows of df below
header("3. df.head(5)")
print(df.head(5))
header("3. df.tail(3)")
print(df.tail(3))

# Getting Data Types, index, columns, values below
header("4. df.dtypes")
print(df.dtypes)
header("4. df.index")
print(df.index)
header("4. df.columns")
print(df.columns)
header("4. df.values")
print(df.values)

# Statistical summary of each column - !THIS IS VERY USEFULL! - below
header("5. df.describe()")
print(df.describe())

# sorting records by any column. Using the column name you can sort the entire DF using that data alone. below
header("6. df.sort_values('record_high', ascending=False" )
print(df.sort_values('record_high', ascending= False))

# Slicing Records below
header("7.slicing -- df.avg_low")
print(df.avg_low)
header("7. slicing -- df['avg_low]")# This one and the one above do the exact same thing
print(df['avg_low'])
header("7. slicing -- df[2:4]") # index with single column
print(df[2:4])                  # rows 2 to 3
header("7. slicing -- df[['avg_low','avg_high']]") # slices at multiple column names
print(df[['avg_low', 'avg_high']])
header("7. slicing -- df.loc[:,['avg_low','avg_high']]") # this is dr.location or dr.loc syntaxtualy
print(df.loc[:, ['avg_low', 'avg_high']])   # multiple columns: df.loc[from_row:to_row,['column1', 'column2']
header("7. slicing scalar value -- df.loc[9,['avg_precipitation']]")
print(df.loc[9, ['avg_precipitation']]) # index location can receive range or list of indices. [0:n] or a range.
header("7. df.iloc[3:5,[0,3]]") #index location
print(df.iloc[3:5, [0,3]])

# Filtering Below
header("8. df[df.avg_precipitation > 1.0]") #filter on column values
print(df[df.avg_precipitation > 1.0])
header("8. df[df['month'].isin(['Jun', 'Jul', 'Aug'])]")
print(df[df['month'].isin(['Jun', 'Jul', 'Aug'])])

# Assignment -- very similar to slicing
header("9. df.loc[9,['avg_precipitation']] = 101.3")
df.loc[9,['avg_precipitation']] = 101.3
print(df.iloc[9:11])

header("9. df.loc[9,['avg_precipitation']] = np.nan") # nan = not a number. you can asign things to not be a number
df.loc[9,['avg_precipitation']] = np.nan
print(df.iloc[9:11])

header("9. df.loc[:,'avg_low'] = np.array([5] * len(df))") # for all rows of avg_low switch them over to 5. all values are now 5 in avg_low
df.loc[:,'avg_low'] = np.array([5] * len(df))
print(df.head())

header("9. df['avg_day'] = (df.avg_low + df.avg_high) / 2") # makes a new column called avg_day that takes information from the existing data and divides it by 2, to get the average value for that new column.
df['avg_day'] = (df.avg_low + df.avg_high) / 2
print(df.head())

# 10. renaming columns
header("10. df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)") # the inplace operator just saves the changes to the variable df.
df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)		# rename 1 column    #df = df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True) also works
print(df.head())

header("10. df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']") # Easy way to just mass change the column names
df.columns = ['month','av_hi','av_lo','rec_hi','rec_lo','av_rain','av_day']
print(df.head())

# # 11. iterate a df
# header("11. iterate rows of df with a for loop")
# for index, row in df.iterrows():
#     print (index, row["month"], row["avg_high"])
#
# # 12. write to csv file
# df.to_csv('foo.csv')
























