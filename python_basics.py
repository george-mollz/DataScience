
#26/07/23
if 5  > 2 : 

   #casting the data type values of varibles
   a=float(3)#type float
   b=bool(5>2)#type boolean

   #snake case variable
   my_Name_Is = "JUMA"

   #assigning many values to multiple varibles
   p,q,r = "orange", 1 , float(400) 

   #one value to multiple variables
   o=i=u = "AM I A PROGRAMMER"

   #this is assignemnt 
   x=5#this is type int 
   #assining x with a new value to see what the output will be
   y="Hello,World"#this is type String 

   #creating a list
   myList = ['one','two','three']

   #counting number of elements
   qw=myList.count("two")
   print(qw)


   #creating a new list
   carList = ['Ford','Mercedez','Isuzu']
   
   carList.extend(myList)#extending carList to myList
   print(carList)

   #appepind suzuki
   carList.append("Suzuki")
   print(carList)

   print(myList)#printing the list

   myList.reverse()#reversing the order of the values of mylist
   print(myList)

   x=myList.index("one")
   print(x)#obtaining the index of an item

   y=myList.insert(2,"Replaced")
   print(y)

   myList.sort()#sorting the myList
   print(myList)

   myList.pop(1)#popping second variable
   print(myList)
   
   
   myList.clear()#clearing the list
   print(myList)

  
   
   #unpacking list
   fruits = ["orange" , bool(6>20) , 1]#packing list
   l,m,n = fruits
   print(l)
   print(m)
   print(n)

   #printing strings and values of variables
   print("five is greater than two")
   print("hallo  world")
   print(a)
   print(b)
   print(x)
   print(y)
   print(my_Name_Is)
   print(p)
   print(q)
   print(r)
   print(o)
   print(i)
   print(u)
   
   #obtaining the data type values for the uncasted variable
   print(type(a))
   print(type(b))
   print(type(x))
   print(type(y))
   """
   this 
   is 
   a 
   multiple 
   line 
   comment
   """

   #dealing with TUPLES
   myTuple = ("apple","banana","cherry")
   print(myTuple)
   print(len(myTuple))

   thisTuple=("apple",1,True)
   print(type(thisTuple))

   #tuple constructor
   thisTuple = tuple(("apple","banana","cherry","berry"))
   print(thisTuple)

   #accessing tuple items
   print(thisTuple[2])#accessing the second item in the tuple
   print(thisTuple[-3])#accessing the second last item in the tuple
   print(thisTuple[0:2])#selecting range of tuples: index 0 included but index 2 not included
   print(thisTuple[2:])#prints all values from index 2 to the end

   #range of negative indexes 
   print("RANGE OF NEGATIVE INDEXES")
   thisTuple = tuple(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"))
   print(thisTuple[-4:-1])
   print(thisTuple[-1:-4])#this order does not exist since tuples are unchangeable

   #checking in an item exists in a tuple
   if "cherry" in thisTuple:
      print("yes,'banana' is in the fruits tuple")

   #updating tuples
   """
   to modify a tuple 
   change it to list 
   select specific index item to modify
   then modify it
   lastly change it back 
   to a tuple
   """
   y = list(thisTuple)  
   y[2]="Parachichi"
   thisTuple = tuple(y) 
   print(thisTuple)

   #adding an item to a tuple
   """
   the same as update
   but this time
   no selecting any item
   just append 
   """
   y = list(thisTuple)
   y.append("sweetMelon")
   thisTuple=tuple(y)
   print(thisTuple)

   #adding a tuple to a tuple 
   y = ("Lemon",)
   thisTuple += y
   print(thisTuple)

   #remove item(s) from a tuple
   """
   same as modify but
   this time 
   remove an item by specifying the 
   """
   y=list(thisTuple)
   y.remove("Lemon")
   thisTuple=y
   print(thisTuple)





   #27/07/23

   #unpacking tuples
   """
   in python the number of 
   variables must match the number 
   of values in the tuple
   """

   """
   If NOT it is required to use an asterisk 
   to collect the remaining values
   as a list 
   """

   #when variables and values match in the tuple
   fruits = ("WaterMelon","Orange","Ovacado")
   (x,y,z)=fruits
   print(x)
   print(y)
   print(z)

   #when values exceed variables in the tuple
   fruits = ("WaterMelon","Orange","Ovacado","Banana","Fig","Berry","Grapes")
   (x,y,*z)=fruits#the asterick can stay with any variable and provides respective list 
   print(x)
   print(y)
   print(z)



   #LOOP TUPLES
   #iterating through items using FOR LOOP
   print("\n")
   thisTuple = (2,3,4,5,6,7,8,9,10,1)   
   print("LOOP  TUPLES")
   for x in thisTuple:
      print(x)#displaying all tuple items

   print("\n")
   print("RANGE TUPLES ")  
   for i in range(len(thisTuple)):
      print(thisTuple[i])#range is used to refer an item from its respective index

   print("\n")
   print("WHILE LOOP")
   #we are still using the above tuple
   i=0
   while i < len(thisTuple):
      i=i+1
      print(i)

   print("\n")
   #joining tuples
   print("JOINING TUPLES")
   tuple1 = (10,11,12)
   tuple2 = (13,14,15)

   tuple3 = tuple1 + tuple2
   print(tuple3)


   print("\n")
   print("MULTIPLY TUPLES")#does not execute the items value but deal with number of repeatitions of the tuples
   myTuple = tuple3 * 2#the items will be written twice
   print(myTuple)


   #TUPLE METHODS
   print("TUPLE METHODS")
   print("COUNT")#returns the number of times an item appears in the tuple
   x = myTuple.count(13)
   print(x)
   print("INDEX")#returns the index of an item in the tuple
   x=myTuple.index(13)
   print(x)


   #SETS
   print("\n")
   print("SET")#stores multiple items in a single variable
   mySet = {"Math","Kiswahili","Spanish","English","German","German"}
   #sets are written with curly brackets
   #Unordered meaning we are not certain 
   #what order the items will appear
   #unchangeable
   #No duplicates, if occurs it will be ignored
   print(mySet)

   #True and 1 are treated as same value
   thisSet= {"apple","banana","cherry",True,1,2}
   print(thisSet)


   #what about False and 0
   thisSet = {False,0,4}
   print(thisSet)#yes False and 0 are same thing in sets

   #length of set
   print(len(thisSet))

   #obtain data type of values in a tuple
   print(type(thisSet))

   #set constructor
   thisSet = set(("apple","banana","cherry"))
   print(thisSet)

   #accessing set items
   #you cannot just refer to an index or a key
   #loops are convinient or use an "in" keyword
   for x in thisSet:#using for loop
      print(x)

   #using in keyword
   print("cherry" in thisSet)#returns boolean   

   #you can only add items to a set but not be able to change them


   #Adding items to a set
   #use the add method
   thatSet = {"nmb","crdb","nbc"}
   print(thatSet)

   print("\n")
   print("ADDING AN ITEM(s) TO AN EXISTING SET")
   thatSet.add("stanbic")#Adding item stanbic
   print(thatSet)

   print("\n")
   print("ADDING SET(S) TO AN EXISTING SET")
   #adding sets
   accounts = {"savings","checking"}
   
   thatSet.update(accounts)
   print(thatSet)


   print("\n")
   print("REMOVING AN ITEM OF THE SET")
   thatSet.remove("nbc")
   print(thatSet)

   #or use the "discard" word 
   thatSet.discard("crdb")
   print(thatSet)

   #using pop() provides uncertainty which item is removed
   thatSet.pop()
   print(thatSet)

   #clear() empties the whole set
   thisSet.clear()
   print(thisSet)

   #Deleting the set using del keyword
   del thatSet
   
   print("\n")
   #JOIN TWO SETS
   print("JOIN TWO SETS")
   #union() or update()
   set1 = {"a","b","c"}
   set2 = {1,2,3}

   set3 = set1.union(set2)#using union()
   print(set3)

   #using update()
   set1.update(set2)
   print(set1)

   print("\n")
   print("INTERSECTION OF SETS")
   #intersecting two sets
   #intersection_update() returns common item(s) of the two sets
   x={1,2,4}
   y={"google","microsoft","apple"}
   x.intersection_update(y)
   print(x)#provides nothing since there is no common item

   x={1,2,4,"google"}
   y={"google","microsoft","apple"}
   x.intersection_update(y)#returns 'google' since it is found in both sets
   print(x)

   print("\n")
   print("SYMMETRIC DIFFERENCE")
   x={1,2,4,"google"}
   y={"google","microsoft","apple"}
   x.symmetric_difference_update(y)
   print(x)

   #SET METHODS
   #difference
   print("\n")
   print("DIFFERENCE")
   x={1,2,4,"google"}
   y={"microsoft","apple"}
   x.difference(y)#returns only values of the set x but not set y 
   print(x)

   print("\n")
   print("DIFFERENCE UPDATE")
   x={1,2,4,"google"}
   y={"google","microsoft","apple"}
   x.difference_update(y)#removes items in this set that are included in the other set
   print(x)

   print("\n")
   #DICTIONARY
   print("DICTIONARY")
   thisDict = {
      #key : value
      "brand" : "Suzuki",
      "model" : "Vitara",
      "Year"  : 2005
       }
   print(thisDict)

   print("\n")
   print("accessing dictionary")
   x=thisDict["brand"]# always refer to the key name 
   print(x)

   #using get() to access items
   x=thisDict.get("model")
   print(x)

   #change values
   thisDict["model"] = "JIMMY"
   print(thisDict["brand"],thisDict["model"])

   #loop through a dictionary 
   for x in thisDict:
      print(x)

   #obtaining the values of the dictionary using values()
   for x in thisDict.values():
      print(x)
      
   #to loop through both keys and values items()
   for x,y in thisDict.items():
      print(x,y)

   #adding a new key with its respective value
   thisDict["colour"]="red"

   #removing items in a dictionary using a pop() function
   thisDict.pop("colour")
   print(thisDict)

   #dictionary length
   print(len(thisDict))

   #checking data type  in dictionary
   print(type(thisDict))  

   #dictionary constructor
   myDictionary = dict(brand="Toyota",model="GXR",Year="2022")
   print(myDictionary)

   #using keys() to obtain a list of all keys 
   x = myDictionary.keys()
   print(x)

   if "model" in myDictionary:
      print("yes, ' model' is one the keys in the myDictionary")

   #changing items in  
   # 

   #FILE FORMAT
   f= open("demoFile.txt","rt")  
   print(f.read())

   x= [1,2,3,4,5,6]

   for u in x:
      pass