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
