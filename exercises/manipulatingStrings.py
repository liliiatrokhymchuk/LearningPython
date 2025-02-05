while True:
    print("Enter your age:")
    age = input()
    if (
        age.isdecimal()
    ):  # isdecimal Returns True if the string consists only of numeric characters and is not blank
        break
    print("Enter a number")


while True:
    print("Enter your password:")
    password = input()
    if (
        password.isalnum()
    ):  # isalnum() Returns True if the string consists only of letters and numbers and is not blank
        break
    print("Enter only numbers and/or letters")


# The join() and split() Methods
name = " ".join(["My", "name", "is", "Lily"])
print(name)

name2 = "My name is Lily".split()
print(name2)


hello = "Hello".upper().isupper()
print(hello)
