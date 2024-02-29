#Python inbuild datatypes
# 1. List 
#In list data type, you can modify the values during run time
a = [] #Example of an empty list
a = [1, 2, 3, 'gen']  #This is an example of a list
b = 3
print(type(a))
print(a[0]) #This is finding out the index value
print(a[2])

# Method of adding items in list
# 1. Append (Method of list) 
#Append stores data in the last for a list datatype
a.append("is hot")
print(a)

x = []
x.append(1)
print(x)

k = input("Number 1 ")
l = input("Number 2 ")
m = input("Number 3 ")

word = []

word.append(2)
word.append(3)
word.append(4)

print(word)
print(len(word))  #We can use len to count the number of values in a list

#2. Insert  
g = [-1, 3, 5, 7]
print(g[-3]) #Using minus value reverses #We can also using minus value to count the last value
g.insert(2, "sangen") #Insert (This is used to add value in a list)

#3. Concat 
first = [1, 2, 3, 4]
second = [5, 6, 7, 8]
print(first+second) #This is how to concat #Baically just add two lists

a = [1,1,1,1,1,1,1,1,2,2,2,2,3,4,4,5]
a.remove(5)

# Mutable = Datatype that can be changed during the python run time
# Immutable = That can't be changed

a = [1,2,3,4,5,6,7]
a.remove
a.clear()
print(a)
del a[5] 

#clear = We use this function to remove the list of a varible

# Slicing = :
list[startslicingindex : lastsclicingindex]


t = [2,4,6,8,10]
print(t[2:4])




