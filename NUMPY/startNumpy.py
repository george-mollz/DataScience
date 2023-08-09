import numpy as np
print(np.__version__)#display version of numpy
arr = np.array([1,2,3,4,5,6])
arr0= np.array(42)#0-dimension array
arr1 = np.array([1,2,3,4,5])#1-dimension array and most common array, contains 0-dimension elements
arr2 = np.array([[1,2,3],[4,5,6]])#2-dimension array contains 1-dimension elements
arr3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])#3-dimension array contains 2- dimension elements

#printing arrays 
print(arr0)
print(arr1)
print(arr2)
print(arr3)

#printing dimensions of arrays 
print(arr0.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

#creating an array with 5-dimensions
arr=np.array([1,2,3,4],  ndmin=5)
print(arr)
print('number of dimensionn :', arr.ndim)

print("\n")
#array indexing 
arr = np.array([1,2,3,4,5])
print(arr[1])# printing the second element of the matrix

print("\n")
#adding elements of matrices 
print(arr[0] + arr[1])

print("\n")
#Accessing 2-D array element
#accessing the first row and second column
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0,1])

print("\n")
#accessing 3-D array element
#Accessing the third element of the second array of the first array
arr = np.array([
    [[1,2,3],[4,5,6]],
                [[7,8,9],[10,11,12]]
                ])
print(arr[1,0,2])#third element of fist array of the second array:element 9


print("\n")
#negative indexing 
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[1,-1])



print("\n")
print("SLICING ARRAYS")
#slicing array:means taking element(s) from one index to another index
arr = np.array([1,2,3,4,5,6,7])
print(arr[3:6])
print(arr[4:])
print(arr[:4])#4 not include
print(arr[-3:-1])#-1 not included





print("\n")
print("STEP")
#STEP 
#1-D array
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print(arr[1:19:3])#the step=3 is the interval of indices of 3
print(arr[::2])#returns all element with index interval of 2 

print("\n")
#2-D array
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0, 1:4:2])
#returning index 2 for both elements
print(arr[0:2 , 2])

print("\n")
#from both elements slicing index 1 to index 4(not included) return 2-D array
print(arr[0:2, 1:4])


print("\n")
#DATA TYPES
print(" DEFINED DATA TYPES")
arr = np.array([1,2,3,4])
print(arr.dtype)
print(type(arr))

print("\n")
#creating arrays with a defined data type
print("STRING")
arr = np.array([1,2,3,4,5], dtype='S')#STRING
print(arr)
print(arr.dtype)
print(type(arr))

print("\n")
print("FLOAT")
arr = np.array([1,2,3,4,5], dtype='f')#FLOAT
print(arr)
print(arr.dtype)
print(type(arr))

print("\n")
print("INTEGER")
arr = np.array([1,2,3,4,5], dtype='i')#INTEGER
print(arr)
print(arr.dtype)
print(type(arr))

"""
print("\n")
arr = np.array([1,2,3,4,5], dtype='u')
print(arr)
print(arr.dtype)
print(type(arr))
"""

print("\n")
arr = np.array([1,2,3,4,5], dtype='U')
print(arr)
print(arr.dtype)
print(type(arr))

print("\n")
arr = np.array([1,2,3,4,5], dtype='i4')
print(arr)
print(arr.dtype)
print(type(arr))





#WHAT IF A VALUE CANNOT BE CONVERTED
"""
print("\n")
arr = np.array(['a','2','3','4','5'], dtype='i')
print(arr)
print(arr.dtype)
print(type(arr))
"""
#the best way to convert is use the astype() method
arr = np.array([1.1, 2.1, 3.1])

newArr = arr.astype('i')

print(newArr)
print(newArr.dtype)

#from interger to boolean
arr = np.array([1, 0, 3])

newArr = arr.astype(bool)

print(newArr)
print(newArr.dtype)






print("\n")
#NUMPY ARRAY COPY vs VIEW
#COPY: does own the data in which made to it does not change the original array
arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

print("\n")
#VIEW: does NOT own the data in which changes made to it affects the original array
arr = np.array([1,2,3,4,5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

print("\n")
#checking if array owns data using "base" attribute and returns "none" if the array owns the data
arr = np.array([1,2,3,4,5])
x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)


print("\n")
#NUMPY ARRAY SHAPE
#shape: number of elements in each dimension
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
x = arr.shape
print(x)

print("\n")
#shape of a multi-dimensional array
arr = np.array([1,2,3,4,5],ndmin=5)

print(arr)
print('shape of array :', arr.shape)

print("\n")
#RESHAPING FROM 1-D TO 2-D
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newArr = arr.reshape(4,3)
print(newArr)

print("\n")
#RESHAPING FROM 1-D TO 3-D
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newArr = arr.reshape(2,3,2)
print(newArr)
print(newArr.base)#checks whether the array owns the data or not 

print("\n")
#unknown dimension
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newArr = arr.reshape(2,2,-1)
print(newArr)

print("\n")
#flattening the arrays: converting a multidimensional array into a 1-D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
newArr = arr.reshape(-1)
print(newArr)



print("\n")
#ITERATING ARRAYS
#1-D ARRAY
arr = np.array([1,2,3])

for x in arr:
    print(x)


print("\n")
#2-D ARRAY
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    print(x)



print("\n")
#3-D ARRAY
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
    for y in x:
        for z in y:
            print(z)
           


print("\n")
#for arrays with high dimensionality
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
    print(x)

print("\n")
print("ITERATING AN ARRAY USING DIFFERENT DATA TYPES")
#iterating an array with different data types
arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)

print("\n")
#iterating with different step size
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8],[9,10,1,3],[5,3,8,3]])
"""
for x in np.nditer(arr[:, ::2]):
    print(x)
"""
for x in np.nditer(arr[:, ::2]):
    print(x)


print("\n")
print("ENUMERATED ITERATION USING ndenumerate()")
#Enumerated Iteration Using ndenumerate()
#enumeration means mentioning sequence number of somethings one by one
arr = np.array([1,2,3])

for idx, x in np.ndenumerate(arr):
    print(idx, x)

print("\n")
arr = np.array([[[[[1,2,3,4],[5,6,7,8]]]]])

for idx, x in np.ndenumerate(arr):
    print(idx, x)




print("\n")
print("NUMPY JOINING ARRAY")
#NumPy Joining Array
#joining means putting contents of two or more arrays in a single array
#in numpy we join arrays using "axes" while in SQL we join arrays based on a "key"
arr1 = np.array([1,2,3])

arr2 = np.array([4,5,6])

arr = np.concatenate((arr1,arr2))

print(arr)




print("\n")
print("JOINING TWO 2-D ARRAYS ALONG ROWS(AXIS=1)")
#joining two 2-D arrays along rows(axis=1)
arr1 = np.array([[1,2],[3,4]])

arr2 = np.array([[5,6],[7,8]])

arr = np.concatenate((arr1,arr2), axis=1 )

print(arr)


print("\n")
print("JOINING ARRAYS USING STACK FUNCTIONS")
#joining arrays using stack functions
#Stacking is equivalent to Concatination, difference is that stacking is done along a new axis

