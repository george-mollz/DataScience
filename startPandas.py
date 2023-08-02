import pandas as pd 

mydataset = {
    'cars' : ["BMW", "Volvo", "Ford"],
    'passings' : [3,7,2]
}
myvar = pd.DataFrame(mydataset)
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
calories = {"day":420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)