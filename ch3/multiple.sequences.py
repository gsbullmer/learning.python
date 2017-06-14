# data
people = ['Jonas', 'Julio', 'Mike', 'Mez']
ages = [25, 30, 31, 39]
nationalities = ['Belgium', 'Spain', 'England', 'Bangledesh']

# simple way
for position in range(len(people)):
    person = people[position]
    age = ages[position]
    print(person, age)
print()

# enumerate
for position, person in enumerate(people):
    age = ages[position]
    print(person, age)
print()

# zip
for person, age in zip(people, ages):
    print(person, age)
print()

# explicit
for person, age, nationality in zip(people, ages, nationalities):
    print(person, age, nationality)
print()

# implicit
for data in zip(people, ages, nationalities):
    person, age, nationality = data
    print(person, age, nationality)
print()

# while
position = 0
while position < len(people):
    person = people[position]
    age = ages[position]
    print(person, age)
    position += 1
