import pandas as pd

s2 = pd.Series([1, 2, 3, 4, 5])
print(s2)
print(s2.index)
print(s2.values)

# index
scores = pd.Series([1, 3, 4, 2, 6], index=["Name1", "Name2", "Name3", "Name4", "Name5"])
print(scores)
print(scores.index)
print(scores.values)

# dictionaries
d = {"Name1": 1, "Name2": 3, "Name3": 4, "Name4": 2, "Name5": 6}
s3 = pd.Series(d)
print(s3)
print(s3.index)

s5 = pd.Series(
    d, index=["Name1", "Test", "Name3", "Name4", "Test1"]
)  # here there is no value corresponding to new names in our dictionary d(result for Test is NaN)
print(s5)


# Data Frame
df1 = pd.DataFrame()
print(df1)
# print(df1.columns)
print(df1.index)  # empty index object

# list
students_list = [
    ["Name1", "Lastname1", 23, "Chemistry", 86],
    ["Name2", "Lastname2", 22, "Art", 99],
    ["Name3", "Lastname3", 25, "Math", 86],
    ["Name4", "Lastname4", 28, "Biology", 74],
]
students_df = pd.DataFrame(students_list)
students_df = pd.DataFrame(
    students_list, columns=["First_Name", "Last_Name", "Age", "Major", "Score"]
)
print(students_df)
print(students_df.shape)  # how many rows/columns df has

# dictionary
students_dictionary = {
    "First_Name": ["Name1", "Name2", "Name3", "Name4"],
    "Last_Name": ["LastName1", "LastName2", "LastName3", "LastName4"],
    "Age": [21, 22, 23, 24],
    "Major": ["Art", "Biology", "Math", "Chemistry"],
}
students_df2 = pd.DataFrame(students_dictionary)
print(students_df2)
print(students_df2.head(2))  # to check specified number of first rows in df
print(students_df2.tail(2))  # last rows

print(students_df2.info())  # check the num of columns, datatype, etc.
print(students_df2.describe())  # check basic statistic info of our numerical data
