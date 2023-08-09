import pandas as pd 
import matplotlib.pyplot as plt







mydataset = {
    'cars' : ["BMW", "Volvo", "Ford"],
    'passings' : [3,7,2]
}
myvar = pd.DataFrame(mydataset)#Datasets to be discussed later...
print(myvar)

print("\n")
print("checking version of panda")
#checking pandas version
print(pd.__version__)





print("\n")
print("SERIES ")
#SERIES
a = [1,7,2]
myvar = pd.Series(a)
print(myvar)








print("\n")
print("LABELS")
#LABELS
print(myvar[0])
print(myvar[1])

print("\n")
print("CREATING LABELS")
#CREATING LABELS
a = [1,7,2]
myvar = pd.Series(a, index = ["x" , "y", "z"])
print(myvar)

print("\n")
print("ACCESSING ITEM REFERRING TO LABEL")
#ACCESSING ITEM REFERRING TO LABEL
print("y")

print("\n")
print("Key/Value Ojects as Series")
#Key/Value Ojects as Series
calories = {"day1":420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

print("\n")
print("SELECTING ONLY SOME OF THE ITEMS IN THE DICTIONARY ")
#SELECTING ONLY SOME OF THE ITEMS IN THE DICTIONARY
myvar  = pd.Series(calories, index=["day1","day2"])
print(myvar)





























print('\n')
print("\n")
print("DATA FRAMES")
#DATA FRAMES
data = {
    "calories": [420,380,390],
    "duration": [50,40,45]
}
#load data into dataFrame object:
df = pd.DataFrame(data)#contains two series: calories and duration
print(df)

print("\n")
print("LOCATE ROW")
#LOCATE ROW using .loc[rowIndex] function
print(df.loc[0])

print("\n")
print(df.loc[[0,1]])#returns first row and second row

print("\n")
print("NAMED INDEXES")
#NAMED INDEXES
#Instead of using integer indices let us name as we desire
df = pd.DataFrame(data, index=["a","b","c"])
print(df)

print("\n")
print("LOCATING NAMED INDEXES")
#LOCATING NAMED INDEXES
print(df.loc["b"])#returns values for the respective row


print("\n")
print("LOADING FILE INTO A DATAFRAME")
#LOADING FILES INTO A DATAFRAME

print("EXCEL FILES")
df = pd.read_excel("E:\APPLICATIONS\VSCODE\PROJECTS\PYTHON\DataScience\PANDAS\Badly-Structured-Sales-Data-2.xlsx")
print(df.info())
print("\n")
print("DISPLAYING EXCEL DATA")
print(df)



print("\n")
print("CSV files")
df = pd.read_csv("E:\APPLICATIONS\VSCODE\PROJECTS\PYTHON\DataScience\PANDAS\data.csv")
print(df)#reads all the rows of a dataFrame
print(df.head())#reads first five rows of a dataFrame
print(df.tail())#reads last five rows of a dataFrame


print("\n")
print("JSON files")
#JSON
df = pd.read_json("E:\APPLICATIONS\VSCODE\PROJECTS\PYTHON\DataScience\PANDAS\data.json")
print(df)#reads all data


print("\n")
print("READING FIRST FIVE ROWS")
print(df.head())#reads first five data
print("\n")
print("READING LAST FIVE ROWS")
print(df.tail())#reads last five data

print("\n")
print("LOADING THE WHOLE JSON file INTO A DATAFRAME")
#loading the json file into a DataFrame
df = pd.read_json('E:\APPLICATIONS\VSCODE\PROJECTS\PYTHON\DataScience\PANDAS\data.json')
print(df.to_string())#prints the entire dataFrame

print("\n")
print("DICTIONARY AS JSON")
#dictionary as JSON
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)
print(df)


print("\n")
print("ANALYZING DATAFRAMES")
#Analyzing DataFrames
df = pd.read_csv("E:\APPLICATIONS\VSCODE\PROJECTS\PYTHON\DataScience\PANDAS\data.csv")
print("READING 20 FIRST ROWS")
print(df.head(20))#by specifying first n rows it returns first n rows 
print("READING 20 LAST ROWS")
print(df.tail(20))#by specifying last n rows it returns last n rows


print("\n")
print("INFO ABOUT THE DATA")
#info about the data
print(df.info())
















#CLEANING EMPTY CELLS
print("\n")
print("\n")
print("CLEANING EMPTY CELLS")
print("\n")
print("EXCEL FILES")
df = pd.read_excel("E:\APPLICATIONS\VSCODE\PROJECTS\PYTHON\DataScience\PANDAS\Badly-Structured-Sales-Data-2.xlsx")
print(df.info())
print("\n")
print("DISPLAYING EXCEL DATA")
print(df)
print("\n")
print("DISPLAYING SUMMARY INFORMATION ABOUT THE EXCEL DATA")
print(df.info())

#REMOVING ROWS
print("\n")
print("REMOVING ROWS")
new_df= df.dropna()
print(new_df.to_string())

print("\n")
print("DISPLAYING NEW INFORMATION ON THE NEW DATAFRAME")
print(new_df.info())


#removing rows with inplace=true and does not return a new dataframe
print("\n")
print("REMOVINF ROWS USING 'INPLACE=TRUE'")
print("DISPLAYING EXCEL DATA")
df = pd.read_excel("E:\APPLICATIONS\VSCODE\PROJECTS\PYTHON\DataScience\PANDAS\Badly-Structured-Sales-Data-2.xlsx")
print("\n")
print("DISPLAYING SUMMARY INFORMATION ABOUT THE EXCEL DATA")
print(df.info())
print("\n")
print("USING THE INPLACE=TRUE")
print(df.dropna(inplace=True))
print("DISPLAYING DATA INFO AFTER REMOVING ROWS")
print(df.info())


#REMOVING EMPTY VALUES
print("\n")
print("REPLACING EMPTY VALUES USING 'fillna(n,inplace = True)")
#obtaining the excel file
df = pd.read_excel("E:\APPLICATIONS\VSCODE\PROJECTS\PYTHON\DataScience\PANDAS\Badly-Structured-Sales-Data-2.xlsx")
#replacing empty values with inplace = True
df.fillna(130,inplace = True)
print(df.head(20))#lets see the first twenty rows



#replacing only for specified columns
print("\n")
print("REPLACE ONLY FOR SPECIFIED COLUMNS")
#obtaining the excel file
df = pd.read_excel("E:\APPLICATIONS\VSCODE\PROJECTS\PYTHON\DataScience\PANDAS\Badly-Structured-Sales-Data-2.xlsx")
#replacing empty values for specified columns: First class
print("FIRST CLASS column")
df["First Class"].fillna(130,inplace = True)
print(df.head(30))#displaying the first 30 entries


#replacing using MEAN, MODE or MEDIAN
print("\n")
print("REPLACE USING MEAN, MODE or MEDIAN")
#obtaining the excel file
df = pd.read_excel("E:\APPLICATIONS\VSCODE\PROJECTS\PYTHON\DataScience\Badly-Structured-Sales-Data-2.xlsx")
#replacing empty values with MEAN
print("MEAN")
x = df["First Class"].mean()
df["First Class"].fillna(x,inplace = True)

print(df.head(30))#displaying the first 30 entries



print("\n")
#obtaining the excel file
df = pd.read_excel("E:\APPLICATIONS\VSCODE\PROJECTS\PYTHON\DataScience\Badly-Structured-Sales-Data-2.xlsx")
#replacing empty values with MEAN
print("MODE")
x = df["First Class"].mode()
df["First Class"].fillna(x,inplace = True)
print(df.head(30))#displaying the first 30 entries



#obtaining the excel file
df = pd.read_excel("E:\APPLICATIONS\VSCODE\PROJECTS\PYTHON\DataScience\Badly-Structured-Sales-Data-2.xlsx")
#replacing empty values with MEAN
print("MEDIAN")
x = df["First Class"].median()
df["First Class"].fillna(x,inplace = True)

print(df.head(30))#displaying the first 30 entries












"""
print("\n")
print("CLEANING DATA OF WRONG FORMAT")
print("\n")
print("CONVERTING INTO A CORRECT FORMAT")
#obtaining the excel file
"""

print("\n")
print("FIXING WRONG DATA ")
print("REPLACING VALUES")
#Set "First Class" = 409.57 in row 15:
df.loc[15,"First Class"]= 45
print(df.head(16))
 
print("\n")
print("REPLACING VALUES IN LARGER DATASETS")
for x in df.index:
    if df.loc[x,"First Class"] < 120:
        df.loc[x,"First Class"] = 120
print(df.head())        



print("\n")
print("REMOVING ROWS IN LARGER DATASETS")
for x in df.index:
    if df.loc[x,"First Class"] == 120:
        df.drop(x, inplace=True)
print(df.head(90))  





print("\n")
print("REMOVING DUPLICATES")
print(df.duplicated())#returns boolean value

print("\n")
print("DROPPING DUPLICATES")
print(df.drop_duplicates())#the excel does not have duplicates as indicated by the FALSE values
















print("\n")
print("\n")
print("CORRELATION")
#re-using code line 281-287
print("\n")
#obtaining the dataW3.csv file
df = pd.read_json("E:\APPLICATIONS\VSCODE\PROJECTS\PYTHON\DataScience\data.json")
print("SHOWING RELATIONSHIP BETWEEN COLUMNS")
#showing the relationship between columns 
x = df.corr()
print(x)












print("\n")
print("\n")
print("PLOTTING")
#obtaining the dataW3.csv file
df = pd.read_json("E:\APPLICATIONS\VSCODE\PROJECTS\PYTHON\DataScience\PANDAS\data.json")
#plotting the data.json file
df.plot()
plt.show()

print("\n")
print("SCATTER PLOT")
df.plot(kind='scatter', x='Duration', y='Calories')
plt.show()


print("\n")
print("SCATTER PLOT")
df["Duration"].plot(kind='hist')
plt.show()

