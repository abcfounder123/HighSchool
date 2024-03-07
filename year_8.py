"""
list

1. Ordered              ---> index
2. Changeable, mutable  ---> change, delete, update
3. Duplicate values

################################################

a. Append an element
b. Append user input
c. Print a list
d. Append elements using a loop  ( for, while )

################################################

Test.1

This command creates a list:

trees = ["oak", "beech", "willow"]

1. How many elements are in this list?
2. Write the command to append the value
"sycamore" to the list.
3. Write the commands to get user input and add it
to the list.
4. You want the user to add elements to the list, but
you are not sure how many elements. What type
of loop would you use?

################################################

Extra.1

In this lesson you have made two programs
that use loops. One program used a for
loop. A for loop repeats a set number of
times. You set the number to 11 so the
program adds exactly 1 names to the list.
Now make a program that:
• asks the user how many names they want
to add
• loops exactly that number of times.

################################################

e. Index numbers
f. print an element
g. Choose which element to print
h. Choose which element to edit
i. Delete an element
j. Choose which element to delete

################################################

Activity.1

1 Make and run a program to create and edit a list of goals.
2 Make and run a program to:
• create a team list of 11 names (using any method you know)
• allow the user to edit and delete names from the team list.

Extra.2
Amend the program that you made to make and edit a team list. Use a while
loop so the edit and delete commands are repeated.

################################################

Test.2

This command creates a list:
trees = ["oak", "beech", "willow"]
1. What is the value of element index 0?
2. Give the command to delete element index 2.
3. Give the command to change element 1 to "eucalyptus".
4 The user enter this command :
trees[6] = "pine"
This caused an error. Explain why.

################################################

k. Using index numbers
l. out of bounds error ( out of range )
m. Length of a list
n. What numbers are allowed?   ( range )
o. Helpful message
p. Design the message
q. Validation check   ---> if... else, while  ---> insisting on proper input
# crash
# robust program

################################################

Test.3

This command creates a list:
trees = ["oak", "beech", "willow" ]

1. What would be the output of these commands?
number = len(trees)
print(number)

2 Write a print command that will tell the user how to enter a valid
index number.

3 Write the commands to get an index number from the user. Include a helpful
message, for example, the one you thought of for Q2.
4 A programmer wanted to check whether the user input was out of bounds.
Write a logical test which will be True if the index number is valid.

################################################

r. What is a program interface?
---> how the user interacts with the program
---> input, output

Activity.2

Continue the Python program you made in the last lesson. Add code so that the
menu options work properly.
• Append a name. • Print the list.
Remember to include double indentation.
In the next part of the lesson you will develop the program further. You will:
• add new menu options to print, delete and edit elements
• block bad input from the user to avoid an out of bounds error
• sort the list using a new Python function.

################################################

s. procedure / function
t. How to use procedures?
---> Define the procedure/ fun  --->  header(name), body,
---> Call the procedure./ fun   ---> name()


u. modular programming
v. built-in functions
w. A new relational operator/ membership operator  ---> in, not in
x. Using return
y. Linear search algorithm
z. Binary search algorithm


################################################

y. Linear search algorithm
1. Count through the list from the first item.
2. Compare each item to the search term.
3. If there is a match, the item is in the list.

z. Binary search algorithm
1. Sort the list into order.
2. Find the midpoint of the list.
3. Compare the search term to the midpoint. Is it higher or lower?
4. Split the list in half and keep the higher or lower half.

Keep splitting the list in half until it has only one item. (2, 3, 4)

Note ---> The binary search is much faster than the linear search.

################################################################################################

Python

Exercise.1

q.1 Write a python program to find the cubes value from 1 to user input
number. (“The cube of 3 is 27”)

q.2 Find the prime numbers of a number range.

(All prime numbers are greater than 1. If number is less than or equal to 1, it
is not prime. A prime number cannot be divided by any other numbers
without leaving a remainder. Eg./ 13 is prime number. It can only be
divided by 1 and 13.)

eg/ For start range = 25, end range = 50,
Prime numbers between 25 and 50 are: 29, 31, 37, 41, 43, 47

################################################

Exercise.2
1. Print First 10 natural numbers using while loop
2. Write a program to accept a number from a user and calculate the sum of
all numbers from 1 to a given number. (if the user entered 10 the output
should be 55 = 1+2+3+4+5+6+7+8+9+10)
3. Write a program to print the following number pattern using a loop.

picture.1

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5


# picture.2

1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

################################################################################################

# indexing, slicing --> start, stop, step
l = ["apple", "banana", "orange", "strawberry"]

################################################

# access
print(l[-1])
print(l[1:3:1])

################################################

# change
l[-1] = 3
l[1:3:1] = 1, 2
print(l)

################################################

# delete
l = ["apple", "banana", "orange", "strawberry", "apple"]

# remove with value
l.remove("apple")
print(l)

# pop with index
p = l.pop(-2)
print(l)
print(p)

# clear
l.clear()
print(l)

# del l[-1]
del l[1:3:1]  # 1, 2
print(l)

################################################

# add new element
# append
l.append(5)
print(l)

# insert
l.insert(1, "X")
print(l)

################################################
################################################

b. Append user input

# step.1
fruit_list = []

fruit = input("Enter a fruit : ")
fruit_list.append(fruit)
print(fruit_list)

fruit = input("Enter a fruit : ")
fruit_list.append(fruit)
print(fruit_list)

fruit = input("Enter a fruit : ")
fruit_list.append(fruit)
print(fruit_list)

fruit = input("Enter a fruit : ")
fruit_list.append(fruit)
print(fruit_list)


# step.2
def add_fruit():
    fruit = input("Enter a fruit : ")
    fruit_list.append(fruit)
    print(fruit_list)


fruit_list = []
add_fruit()
add_fruit()
add_fruit()
add_fruit()

################################################

d. Append elements using a for loop

# step.3
fruit_list = []
for i in range(5):  #  0 1 2 3 4
    fruit = input("Enter a fruit : ")
    fruit_list.append(fruit)
    print(fruit_list)

################################################

d. Append elements using a for loop

# step.4
fruit_list = []
c = True
while c:
    fruit = input("Enter a fruit : ")
    fruit_list.append(fruit)
    print(fruit_list)

    i = input("Do you want to add another?(yes/ no) : ")
    if i == "no":
        c = False

################################################

# step.5
# 1 2 3 4 5

fruit_list = []

for i in range(1, 6, 1):  # i = 0
    fruit = input(f"{i}.Enter a fruit : ")
    fruit_list.append(fruit)
    print(fruit_list)

print()
print("-" * 40)
print()

fruit_list = []
start = 1
stop = 6
step = 1

i = start
while i < stop:  # i = 0
    fruit = input(f"{i}.Enter a fruit : ")
    fruit_list.append(fruit)
    print(fruit_list)
    i += step

###########

# step.6
# 5 4 3 2 1
fruit_list = []

for i in range(5, 0, -1):  # i = 0
    fruit = input(f"{i}.Enter a fruit : ")
    fruit_list.append(fruit)
    print(fruit_list)

print()
print("-" * 40)
print()

fruit_list = []
start = 5
stop = 0
step = -1

i = start
while i > stop:  # i = 0
    fruit = input(f"{i}.Enter a fruit : ")
    fruit_list.append(fruit)
    print(fruit_list)
    i += step

################################################
################################################

# Year.8 school sample
fruit_list = []
repeat = "yes"

while repeat == "yes":
    fruit = input("\nEnter a fruit : ")
    fruit_list.append(fruit)
    print(fruit_list)
    repeat = input("Do you want to add another?(yes/ no) : ")

################################################

Test.1

This command creates a list:

trees = ["oak", "beech", "willow"]

1 How many elements are in this list?
2 Write the command to append the value
"sycamore" to the list.
3 Write the commands to get user input and add it
to the list.
4 You want the user to add elements to the list, but
you are not sure how many elements. What type
of loop would you use?

1. 3
2. trees.append("sycamore")
3. tree = input("Enter a tree :")
trees.append(tree)
4. while loop

################################################

Extra.1

In this lesson you have made two programs
that use loops. One program used a for
loop. A for loop repeats a set number of
times. You set the number to 11 so the
program adds exactly 1 names to the list.
Now make a program that:
• asks the user how many names they want
to add
• loops exactly that number of times.

fruit_list = []
n = int(input("How many names do you want to add? : "))
for i in range(n):  # 0 1 2 3 4
    fruit = input("Enter a fruit : ")
    fruit_list.append(fruit)
    print(fruit_list)

################################################

# looping purpose    --->   _  (underscore)

fruit_list = []
n = int(input("How many names do you want to add? : "))

for _ in range(n):  # 0 1 2 3 4
    fruit = input("Enter a fruit : ")
    fruit_list.append(fruit)
    print(fruit_list)

################################################

################################################

e. Index numbers

# Indexing ( access, edit, delete )

################################################

g. Choose which element to print

goals = ["pass exams", "help in shop", "buy trainers"]
i = input("which goal do you want to print? : ")  # "1"
i = int(i)  # 1

f. print an element
print(goals[i])  # access

################################################

h. Choose which element to edit

goals = ["pass exams", "help in shop", "buy trainers"]
i = input("which goal do you want to change? : ")
i = int(i)
goals[i] = input("Enter a new goal : ")  # change, edit
print(goals)

################################################

i. Delete an element
j. Choose which element to delete

goals = ["pass exams", "help in shop", "buy trainers"]
i = input("which goal do you want to delete? : ")
i = int(i)
del goals[i]  # delete
print(goals)

################################################

Activities.1

1 Make and run a program to create and edit a list of goals.
2 Make and run a program to:
• create a team list of 11 names (using any method you know)
• allow the user to edit and delete names from the team list.

goals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]   # create by yourself

i = int(input("which goal do you want to edit? : "))
goals[i] = input("Enter a new goal : ")  # change, edit
print(goals)

i = int(input("which goal do you want to delete? : "))
del goals[i]
print(goals)

################################################

goals = ["pass exams", "help in shop", "buy trainers"]
goal = input("which goal do you want to delete? : ")
goals.remove(goal)  # delete by value
print(goals)

################################################

Extra.2

Amend the program that you made to make and edit a team list. Use a while
loop so the edit and delete commands are repeated.

goals = ["pass exams", "help in shop", "buy trainers"]
repeat = "y"
while repeat == "y":
    i = int(input("which goal do you want to edit? : "))
    goals[i] = input("Enter a new goal : ")  # change, edit
    print(goals)

    i = int(input("which goal do you want to delete? : "))
    del goals[i]
    print(goals)

    repeat = input("Do you want to edit and delete? (y / n) :")

################################################

Test.2

This command creates a list:
trees = ["oak", "beech", "willow"]
1. What is the value of element index 0?
2. Give the command to delete element index 2.
3. Give the command to change element 1 to "eucalyptus".
4 The user enter this command :
trees[6] = "pine"
This caused an error. Explain why.

1. "oak"
2. del trees[2]
3. trees[1] = "eucalyptus"
4.
trees = ["oak", "beech", "willow"]   # range =  -3, -2, -1, 0, 1, 2
trees[6] = "pine"
assignment index is out of range, out of bounds

################################################


k. Using index numbers
l. out of bounds error ( out of range )
m. Length of a list
n. What numbers are allowed?   ( range )
o. Helpful message  ( see test.3 )
p. Design the message  ( see test.3 )

q. Validation check   ---> if... else, while  ---> insisting on proper input
# crash
# robust program

colours = ["red", "yellow", "blue", "green"]
i = input("Which color do you choose? :")
i = int(i)
if i < len(colours):
    print(colours[i])
else:
    print("out of bounds error.")

################################################

colours = ["red", "yellow", "blue", "green"]    # -4 to 3   ---> -4 <= i < 4
i = input("Which color do you choose? :")
i = int(i)
t = len(colours)

if -t <= i < t:  # -4 to 3
    print(colours[i])
else:
    print("out of bounds error.")

################################################

# insisting on proper input

colours = ["red", "yellow", "blue", "green"]
i = int(input("Which color do you choose? :"))

while i >= len(colours):
    print("Out of bounds error. Try again.")
    i = int(input("Which color do you choose? :"))

print(colours[i])


colours = ["red", "yellow", "blue", "green"]
i = int(input("Which color do you choose? :"))
t = len(colours)

while not (-t <= i < t):  # (-4 to 3)
    print("Wrong index. Try again.")
    i = int(input("Which color do you choose? :"))

print(colours[i])

################################################

Test.3

This command creates a list:
trees = ["oak", "beech", "willow" ]

1. What would be the output of these commands?
number = len(trees)
print(number)

2 Write a print command that will tell the user how to enter a valid
index number.

3 Write the commands to get an index number from the user. Include a helpful
message, for example, the one you thought of for Q2.
4 A programmer wanted to check whether the user input was out of bounds.
Write a logical test which will be True if the index number is valid.

1.  3
2.  print("Please enter a valid index number ( -3, -2, -1, 0, 1, 2 ).")
3.  i = int(input("Please enter a valid index number ( -3, -2, -1, 0, 1, 2 ) : "))
4.  -t <= i < t

################################################

r. What is a program interface?
---> how the user interacts with the program
---> input, output

Activity.2

Continue the Python program you made in the last lesson. Add code so that the
menu options work properly.
• Append a name. • Print the list.
Remember to include double indentation.
In the next part of the lesson you will develop the program further. You will:
• add new menu options to print, delete and edit elements
• block bad input from the user to avoid an out of bounds error
• sort the list using a new Python function.


menu = '''
TEAM MANAGER
============
This program will help you manage your team.
A: Append a value
B: Print the team list
C: Print one element
D: Delete one element
E : Edit one element
F: Sort the list
X: Exit the program
'''
print(menu)
fruits = []

print("-" * 42)
c = input("Enter your choice :")

while c != "X":
    if c in "ABCDEFX":
        if c == "A":
            print("A: Append a value")
            fruit = input("Enter a fruit : ")
            fruits.append(fruit)

        elif c == "B":
            print("B: Print the team list")
            print(fruits)

        elif c == "C":
            print("C: Print one element")
            i = int(input("which element do you want to print? : "))
            print(fruits[i])

        elif c == "D":
            print("D: Delete one element")
            i = int(input("which element do you want to delete? : "))
            del fruits[i]

        elif c == "E":
            print("E : Edit one element")
            i = int(input("which element do you want to edit? : "))
            fruits[i] = input("Enter a new fruit : ")
            # print(fruits)

        elif c == "F":
            print("F: Sort the list")
            fruits.sort()

        print("-" * 42)
        c = input("Enter your choice :")
        print("-" * 42)

    else:
        print("-" * 42)
        print("Wrong command. Try again.")
        c = input("Enter your choice :")
        print("-" * 42)

################################################

s. procedure / function
t. How to use procedures?
---> Define the procedure/ fun  --->  header(name), body,
---> Call the procedure./ fun   ---> name()

def welcome():
    print("=" * 40)
    print(" " * 12, "WELCOME")
    print("=" * 40)


# welcome()   # calling procedure / function

################################################

u. modular programming

v. built-in functions

import builtins

print(dir(builtins))  # list of built-in functions
print(len(dir(builtins)))
print("sum" in dir(builtins))  # check in built-in list

################################################

atoms = ["Hydrogen", "Helium", "Lithium", "Beryllium",
         "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine",
         "Neon", "Sodium", "Magnesium", "Aluminium", "Silicon",
         "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium",
         "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium",
         "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc",
         "Manganese" "Germanium", "strontium",
         "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine",
         "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium",
         "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium",
         "Palladium", "Silver", "Cadmium", "Indium", "Tin", "Antimony", "Barium",
         "Tellurium", "Iodine", "Xenon", "Cesium", "Barium", "Lanthanum",
         "Cerium", "Praseodymium", "Neodymium", "Promethium", "Samarium",
         "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium",
         "Erbium", "Thulium", "Ytterbium", "Lutetium", "Hafnium", "Tantalum",
         "Tungsten", "Platinum", "Gold",
         "Mercury", "Astatine", "Radon", "Francium", "Radium"]

# in --> relational operator, membership operator
# print("Hydrogen" in atoms)

################################################

atom = input("Enter a atom :")
if atom in atoms:
    print(atom, "is in the list of atoms.")
else:
    print(atom, "is not in the list of atoms.")

################################################

atoms = ["Hydrogen", "Helium", "Lithium", "Beryllium",
         "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine",
         "Neon", "Sodium", "Magnesium", "Aluminium", "Silicon",
         "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium",
         "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium",
         "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc",
         "Manganese" "Germanium", "strontium",
         "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine",
         "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium",
         "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium",
         "Palladium", "Silver", "Cadmium", "Indium", "Tin", "Antimony", "Barium",
         "Tellurium", "Iodine", "Xenon", "Cesium", "Barium", "Lanthanum",
         "Cerium", "Praseodymium", "Neodymium", "Promethium", "Samarium",
         "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium",
         "Erbium", "Thulium", "Ytterbium", "Lutetium", "Hafnium", "Tantalum",
         "Tungsten", "Platinum", "Gold",
         "Mercury", "Astatine", "Radon", "Francium", "Radium"]

# the linear search
# step.1
name = input("Enter a search term: ")   # "A"
stop = len(atoms)

for i in range(stop):  # 0 to 87
    print(i)
    if atoms[i] == name:
        print(name, "found in the list")
        break

################################################

# step.2
def linear_search():
    name = input("Enter a search term: ")  # "A"
    stop = len(atoms)

    for i in range(stop):  # 0 to 87
        # print(i)
        if atoms[i] == name:
            print(name, "found in the list")
            return

################################################

n = int(input("How many times do you want to search? :"))
for _ in range(n):
    linear_search()


repeat = "y"
while repeat == "y":
    linear_search()
    repeat = input("Do you want to search? (y/n) :")

################################################

# step.3
def linear_search_pythonic(l):
    name = input("Enter a search term: ")  # "A"
    for i in l:
        # print(l)
        if i == name:
            print(name, "found in the list.")
            break


linear_search_pythonic(atoms)

################################################
################################################

# binary search

print(2 ** 7)   # 128
print(2 ** 5)  #  32
print(2 ** 6)  #  64
print(2 ** 8)  # 256

#  ans ---> 5, 6, 8

################################################

atoms = ["Hydrogen", "Helium", "Lithium", "Beryllium",
         "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine",
         "Neon", "Sodium", "Magnesium", "Aluminium", "Silicon",
         "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium",
         "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium",
         "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc",
         "Manganese" "Germanium", "Strontium",
         "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine",
         "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium",
         "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium",
         "Palladium", "Silver", "Cadmium", "Indium", "Tin", "Antimony", "Barium",
         "Tellurium", "Iodine", "Xenon", "Cesium", "Barium", "Lanthanum",
         "Cerium", "Praseodymium", "Neodymium", "Promethium", "Samarium",
         "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium",
         "Erbium", "Thulium", "Ytterbium", "Lutetium", "Hafnium", "Tantalum",
         "Tungsten", "Platinum", "Gold",
         "Mercury", "Astatine", "Radon", "Francium", "Radium"]


# background knowledge
atoms.sort()
print(atoms)

midpoint = len(atoms) // 2
print(atoms[:midpoint])
print(atoms[midpoint:])


# str to decimal unicode No
def u(s):
    l = []
    for i in s:
        l.append(ord(i))
    return l


print(u('Aluminium'))
print(u('Antimony'))
print(u('Argon'))
print(u('Arsenic'))

[65, 108, 117, 109, 105, 110, 105, 117, 109]
[65, 110, 116, 105, 109, 111, 110, 121]
[65, 114, 103, 111, 110]
[65, 114, 115, 101, 110, 105, 99]

################################################

# sample from school
def binsearch(atoms):
    atoms.sort()
    name = input("Enter a search term: ")
    while len(atoms) > 1:
        midpoint = len(atoms) // 2
        if name < atoms[midpoint]:
            atoms = atoms[:midpoint]  # left
        else:
            atoms = atoms[midpoint:]  # right

    if atoms[0] == name:
        print(name, "found in the list")
    else:
        print(name, "not found in the list")


binsearch(atoms)

################################################

# check step by step ( school example )

def binsearch(atoms):
    atoms.sort()
    print(atoms, len(atoms))
    name = input("Enter a search term: ")
    while len(atoms) > 1:
        midpoint = len(atoms) // 2
        print(midpoint)
        print(name, "<", atoms[midpoint])
        if name < atoms[midpoint]:
            atoms = atoms[:midpoint]
            print(atoms)
        else:
            atoms = atoms[midpoint:]
            print(atoms)

    if atoms[0] == name:
        print(name, "found in the list")
    else:
        print(name, "not found in the list")

################################################

# pure function
def binsearch(l):
    l.sort()
    name = input("Enter a search term: ")
    while len(l) > 1:
        midpoint = len(l) // 2
        if name < l[midpoint]:
            l = l[:midpoint]  # left
        else:
            l = l[midpoint:]  # right

    if l[0] == name:
        print(name, "found in the list")
    else:
        print(name, "not found in the list")


binsearch(atoms)
print(atoms)

################################################

Exercise.1

q.1 Write a python program to find the cubes value from 1 to user input
number. (“The cube of 3 is 27”)

q.2 Find the prime numbers of a number range.

(All prime numbers are greater than 1. If number is less than or equal to 1, it
is not prime. A prime number cannot be divided by any other numbers
without leaving a remainder. Eg./ 13 is prime number. It can only be
divided by 1 and 13.)

eg/ For start range = 25, end range = 50,
Prime numbers between 25 and 50 are: 29, 31, 37, 41, 43, 47

################################################

# q.1
un = int(input("Enter a number: "))
for n in range(1, un + 1):
    cub = n ** 3
    print("The cube of", n, "is", cub)

################################################

# step.1  ---> checking one number

n = 11  # 1, 11, n > 11,  # 2, 3, 4, 5, 6, 7, 8, 9, 10  # 2, 3, 4, 5,
p = True
for i in range(2, n // 2 + 1):
    print(f"{n} % {i} = {n % i}")
    if n % i == 0:
        p = False
        break

print(p)

################################################

# step.2  --->  checking with function

def is_prime(n):
    p = True
    for i in range(2, n // 2 + 1):
        # print(f"{n} % {i} = {n % i}")
        if n % i == 0:
            p = False
            break
    return p


# test q.2
start = int(input("start range = "))
end = int(input("end range = "))

prime_list = []
for i in range(start, end):
    if is_prime(i):
        prime_list.append(i)

print("Prime numbers between", start, "and", end, "are:", *prime_list)

################################################

start range = 25
end range = 50
Prime numbers between 25 and 50 are: 29 31 37 41 43 47

################################################

Exercise.2

1. Print First 10 natural numbers using while loop
2. Write a program to accept a number from a user and calculate the sum of
all numbers from 1 to a given number. (if the user entered 10 the output
should be 55 = 1+2+3+4+5+6+7+8+9+10)
3. Write a program to print the following number pattern using a loop.

picture.1

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5


# picture.2

1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

################################################
################################################

#  q.1
n = 1
while n <= 10:
    print(n)
    n += 1

################################################

# q.2  ( for )

n = int(input("Enter a number:"))
ans = 0

for i in range(1, n + 1):
    # print(f"{ans} + {i} = ", end="")
    ans += i
    # print(ans)


print("The sum of all numbers from 1 to", n, "=", ans)

################################################

# q.2   ( while )

n = int(input("Enter a number:"))
ans = 0
i = 1

while i < n+1:
    ans += i
    i += 1

print("The sum of all numbers from 1 to", n, "=", ans)

################################################

q.3
picture.1

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

################################################

# step.1      ---> 1 2 3 4 5
print(1, end=" ")
print(2, end=" ")
print(3, end=" ")
print(4, end=" ")
print(5)

################################################

# step.2
for i in range(1, 5+1):
    print(i, end=" ")

################################################

# step.3
n = int(input("\nEnter a number:"))
for i in range(1, n+1):
    print(i, end=" ")

################################################

# step.4
n = int(input("\nEnter a number:"))
for i in range(1, n+1):
    print(i, end=" ")

n = int(input("\nEnter a number:"))
for i in range(1, n+1):
    print(i, end=" ")

n = int(input("\nEnter a number:"))
for i in range(1, n+1):
    print(i, end=" ")

n = int(input("\nEnter a number:"))
for i in range(1, n+1):
    print(i, end=" ")

n = int(input("\nEnter a number:"))
for i in range(1, n+1):
    print(i, end=" ")

################################################

# step.5

n = 1
for i in range(1, n+1):
    print(i, end=" ")

print()

n = 2
for i in range(1, n+1):
    print(i, end=" ")
print()

n = 3
for i in range(1, n+1):
    print(i, end=" ")
print()

n = 4
for i in range(1, n+1):
    print(i, end=" ")
print()

n = 5
for i in range(1, n+1):
    print(i, end=" ")
print()

################################################

# step.5

for n in range(1, 5+1):
    for i in range(1, n + 1):
        print(i, end=" ")

    print()

################################################

# q3, p.1
s = int(input("\nEnter a number:"))
for n in range(1, s+1):
    for i in range(1, n + 1):
        print(i, end=" ")
    print()

################################################
################################################

# picture.2

1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

################################################

n = 5
for i in range(1, n+1):
    print(i, end=" ")

print()

n = 4
for i in range(1, n+1):
    print(i, end=" ")
print()

n = 3
for i in range(1, n+1):
    print(i, end=" ")
print()

n = 2
for i in range(1, n+1):
    print(i, end=" ")
print()

n = 1
for i in range(1, n+1):
    print(i, end=" ")
print()

################################################

# q.3, pic.2

s = int(input("\nEnter a number:"))
for n in range(s, 0, -1):
    for i in range(1, n + 1):
        print(i, end=" ")
    print()

################################################
################################################
"""
