"""Like a list, a dictionary is a mutable collection of many values. But unlike indexes for lists, 
indexes for dictionaries can use many different data types, not just integers. 
Indexes for dictionaries are called keys, and a key with its associated value is called a key-value pair."""

myCat = {"size": "fat", "color": "gray", "disposition": "loud"}
print(myCat)
print(myCat["size"])
print("My cat is " + myCat["color"])

# The keys(), values(), and items() Methods
mydictionary = {"name": "Lily", "age": 32}

# for v in mydictionary.values():
# print (v)
for k in mydictionary.keys():
    print(k)

print(mydictionary)

mydictionary2 = {"name": "Lily", "age": 32}
for i in mydictionary2.items():
    print(i)

mydictionary3 = {"name": "Lily", "age": 32}
print(mydictionary3.keys())
print(list(mydictionary3.keys()))  # list() function


# multiple assignment in a for loop to assign the key and value to separate variables
mydictionary3 = {"name": "Lily", "age": 32}
for k, v in mydictionary3.items():
    print("Key:" + k + " Value:" + str(v))
    print(f"Key: {k} Value: {v}")
print(
    "name" in mydictionary3.keys()
)  # returns boolean. use in/not in operators to see whether a certain key or value exists in a dictionary


# The get() Method. dictionaries have a get() method that takes two arguments:
# the key of the value to retrieve and a fallback value to return if that key does not exist.

mydictionary4 = {"name": "Lily", "age": 32}
print(f"My name is {mydictionary.get('name', 0)}")  # the key exists
print(f"My hobby is {mydictionary.get('hobby', 'Unknown')}")  # the key doesn't exist


# The setdefault() Method. If the key does exist, the setdefault() method returns the key’s value
mydictionary5 = {"name": "Lily", "age": 32}
# if 'hobby' not in mydictionary5:
#    mydictionary5['hobby'] = 'sewing'
mydictionary5.setdefault("hobby", "sewing")
print(mydictionary5)


# Exercises
student_grades = {"Lily": 100, "Name1": 90, "Name2": 80}
for k, v in student_grades.items():
    print(k, v)

student_grades = {"Lily": 100, "Name1": 90, "Name2": 80}
student_grades.setdefault("Name3", 50)
print(student_grades)

student_grades = {"Lily": 100, "Name1": 90, "Name2": 80}
student_grades["Name1"] = 95
del student_grades["Name2"]
print(student_grades)
