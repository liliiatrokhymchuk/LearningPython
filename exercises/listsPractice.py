mylist = ['cat', 'dog', 'rat']
print(mylist[0])
print('Hello, ' + mylist[0])
print(f'Hello, {mylist[0]}')
print(mylist[0:2]) #slice


mylist2 = [['cat', 'dog', 'rat'], [1, 2, 3]]
print(mylist2[1])
print(mylist2[0][2])
print(mylist2[-2])
print(mylist2[0:1]) #slice. The first integer is the index where the slice starts. The second integer is the index where the slice ends.


mylist3 = ['apple', 'orange', 'mango']
print(mylist3[1:])
print(mylist3[:1])
print(len(mylist3))  #length return the number of values that are in a list value passed to it


#Changing Values in a List with Indexes
mylist4 = ['apple', 'orange', 'mango']
mylist3[0] = 'cherry'
mylist3[0] = mylist3[1]
print(mylist3)

#List Concatenation and List Replication
mylist5 = ['apple', 'orange', 'mango']
#mylist5 = mylist5 * 3
mylist5 = mylist5 + ['banana', 'coconut']
print(mylist5)

#Removing Values from Lists with del Statements
mylist6 = ['apple', 'orange', 'mango']
del mylist6[0]
print(mylist6)


#Using for Loops with Lists
for i in [1,2,3,4]:
    print(i)

mylist7 = ['apple', 'orange', 'mango']
for i in range(len(mylist7)):
    print('Index ' + str(i) + ' in mylist7 is: ' + mylist7[i])


#The in and not in Operators
mylist8 = ['apple', 'orange', 'mango']
print('cat' in mylist8)
print('cat' not in mylist8)

#multiple assignment trick (tuple unpacking) is a shortcut that lets you assign multiple
#variables with the values in a list in one line of code
cat = ['fat', 'gray', 'loud']
size, color, disposition = cat
print(size)

"""append and insert. The append() and insert() methods are list methods and can be called 
only on list values, not on other values such as strings or integers"""

mylist9 = ['cat', 'dog', 'bat']
mylist9.append('rat')  #append() method call adds the argument to the end of the list
mylist9.insert(1, 'rabbit') #insert() method can insert a value at any index in the list
mylist9.remove('rat')
print(mylist9)

#sort
mylist10 = ['cat', 'dog', 'bat']
#mylist10.sort()
#mylist10.reverse()
mylist10.sort(reverse=True)
print(mylist10)



#Mutable and Immutable Data Types
#A list value is a mutable data type: it can have values added, removed, or changed. However, a string is immutable: it cannot be changed.


"""The Tuple Data Type. A tuple in Python is an immutable (unchangeable) ordered collection of items. Tuples are similar to lists, 
but once a tuple is created, its elements cannot be modified, added, or removed. Tuples are defined using parentheses ()"""

mytuple = (1, 2, 3, 'Hello')
print(mytuple)
print(mytuple[1])
print(mytuple[1:])


#tuples are immutable, however, if a tuple contains mutable elements (like lists), you can modify the contents of those lists
mytuple2 = (['cat', 'dog', 5], ['you', '8'])
mytuple2[1][1] = 'me'
mytuple2[1].append('they')
print(mytuple2)
print(mytuple2.index(['cat', 'dog', 5]))


#exercise

spam = ['apples', 'bananas', 'tofu', 'cats']
#check if the list is empty:
def is_emply(spam):
    if spam == 0:
        return "This list is empty"

def is_emply(spam):
    if spam == 1:
        return spam[0]

print(spam)
print(is_emply(spam))
