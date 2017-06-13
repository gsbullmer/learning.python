"""objects.py"""

# code block # 1
age = 42
print(age)  # 42
age = 43  # A
print(age)  # 43


# code block # 2
age = 42
print(id(age))  # 1882958208
age = 43
print(id(age))  # 1882958240


# code block # 3
class Person():
    def __init__(self, age):
        self.age = age

fab = Person(age=39)
print(fab.age)  # 39
print(id(fab))  # 1630088392264
fab.age = 29  # I wish!
print(id(fab))  # 1630088392264 # still the same id
