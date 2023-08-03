import pandas as pd 

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
myvar = pd.DataFrame(data)#contains two series: calories and duration
print(myvar)

print("\n")
print(" ")
#