# Regeex are descriptions for a pattern of text
# \d in a regex stands for a digit character

import re  # import regex functions module

# Passing a string value representing regex to re.compile() returns a Regex object
phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")  # r - raw string


# Matching Regex Objects
phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
matchobject = phoneNumRegex.search("My number is 415-555-4242.")
print("Phone number found: " + matchobject.group())


# Grouping with Parentheses
phoneNumRegex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
matchobject = phoneNumRegex.search("My number is 415-555-4242.")
print(
    matchobject.group(1)
)  # (\d\d\d) is group 1. .group(0) or .group() return entire matching set
print(matchobject.groups())  # to retrieve all the groups at once


# Matching Multiple Groups with the Pipe
# By using | and grouping parentheses, we can specify several alternative patterns we'd like regex to match
heroRegex = re.compile(r"Batman|Tina Fey")
matchobject1 = heroRegex.search("Batman and Tina Fey")
print(
    matchobject1.group()
)  # if multiple values matches, the first one only will be return this way

batRegex = re.compile(r"Bat(man|mobile|copter|bat)")
matchobject2 = batRegex.search("Batmobile")
print(matchobject2.group())


# Optional Matching with the Question Mark
# The ? character flags the group that precedes it as an optional part of the pattern
batRegex = re.compile(r"Bat(wo)?man")
matchobject3 = batRegex.search("Batman")
print(matchobject3.group())


# Matching Specific Repetitions with Braces {}
haRegex = re.compile(r"(ha){3}")
matchobject4 = haRegex.search("hahaha")
print(matchobject4.group())

matchobject4 = haRegex.search("ha")
print(matchobject4 == None)


# The findall() Method
phoneNumRegex = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)")  # has groups in parentheses
print(phoneNumRegex.findall("Cell: 415-555-9999 Work: 212-555-0000"))

"""When called on a regex with no groups, such as \d\d\d-\d\d\d-\d\d\d\d, the method findall() returns a list of string matches.
When called on a regex that has groups, such as (\d\d\d)-(\d\d\d)-(\d\d\d\d), the method findall() returns a list of tuples of strings"""


# A regex that matches a number with commas for every three digits
# testNumbers = ["42", "1,234", "6,368,745"]
myRegex = re.compile(r"^\d{1,3}(,\d{3})*$")
matchobject5 = myRegex.search("1,234")
print(matchobject5.group())

# A regex that matches the last name
nameRegex = re.compile("^[A-Z][a-zA-Z]* Lastname$")

testNames = ["Name Lastname", "Test Lastname", "Test2 lastname"]

for name in testNames:
    match = nameRegex.search(name)
    if match:
        print(f"Matched")
    else:
        print(f"Not matched")


# Regex pattern for DD/MM/YYYY
date_regex = re.compile(r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(1\d{3}|2\d{3})$")

# Example date string
date_str = "29/02/2024"

# Searching for a match
match = date_regex.match(date_str)

if match:
    day, month, year = match.groups()
    print(f"Day: {day}, Month: {month}, Year: {year}")
else:
    print("Invalid date format")
