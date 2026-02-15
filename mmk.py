
"""

Procedural programming
1. Sequence
2. Selection (if, elif, else)
3. Loop      (for, while)
4. Function

##########################################

Selection

1. if
   - if code block ( space 4 )
   - condition (right)

2. else
   - else code block ( space 4 )
   - condition (upper first)

3. elif
   - else + if

Exercise
1. All from all , one from one
2. One from all

Knowledge
1. Normal Statement
2. Conditional Statement
3. :   <-- code block, 4 space
4. if code block, else code block
5. not, and, or
6. boolean
7. fotmat (fatr)

####################################################################################

500   -  Doctor
400   -  Engineer
300   -  Math
240   -  Distance

##########################################

Exercise
1. All from all , one from one
2. one from all

##########################################

marks = 550

c1 = marks >= 500          # T
c2 = marks >= 400          # T
c3 = marks >= 300
c4 = marks >= 240

if c1:
    print("Doctor")

if c2:
    print("Engineer")

if c3:
    print("Math")

if c4:
    print("Distance")

##########################################

2. one from all

marks = 550

c1 = marks >= 500          # T
c2 = marks >= 400          # T
c3 = marks >= 300
c4 = marks >= 240

if c1:
    print("Doctor")

if not c1 and c2:
    print("Engineer")

if not c1 and not c2 and c3:
    print("Math")

if not c1 and not c2 and not c3 and c4:
    print("Distance")

##########################################

not c1 and not c2 and not c3 and c4
not c1 and c2
c1
not c1 and not c2 and c3
not c1 and not c2 and not c3 and not c4


c1
not c1 and c2
not c1 and not c2 and c3
not c1 and not c2 and not c3 and c4
not c1 and not c2 and not c3 and not c4

##########################################

marks = 550

c1 = marks >= 500          # T
c2 = marks >= 400          # T
c3 = marks >= 300
c4 = marks >= 240

if c1:
    print("Doctor")

elif c2:
    print("Engineer")

elif c3:
    print("Math")

elif c4:
    print("Distance")

else:
    print("Grade.11")

####################################################################################

Knowledge
1. Normal Statement
2. Conditional Statement
3. :   <-- code block, 4 space
4. if code block, else code block
5. not, and, or
6. boolean
7. fotmat (fatr)

##########################################

5. not, and, or
   - not => opposite
   - and => all True
   - or  => one True

##########################################

6. boolean
   - Empty        => "", 0, 0.0, 0j, [], (), {}, None, ...    --> False
   - any value    => "a", 1, 100, -1, ["Mg Mg", "Aung Aung"]  --> True

##########################################

can buy ?   result = can buy (direct)

if  c1:
    print("you can buy beer.")
    
##########################################

can buy ?   result = can not buy (opposite, not)

if not c1:
    print("you can not buy beer.")

##########################################

if age is greater than 18 and money is enough, show letter "you can buy beer."
if age > 18 and money >= 10000, show letter "you can buy beer."

##########################################

not, and

c1 = age > 18
c2 = money >= 10000
c3 = is_full_moon

can_buy = c1 and c2 and not c3

##########################################

not and or

g1, g2, g3

g1 or g2 or g3

c6 = g6 and basic

g1 or g2 or g3 or g4 or g5 or c6
g1 or g2 or g3 or g4 or g5 or (g6 and basic)

c6 = g6 and not basic
g1 or g2 or g3 or g4 or g5 or not c6
g1 or g2 or g3 or g4 or g5 or not (g6 and not basic)

##########################################

Water moter controller  (not and or)

c1 = low
c2 = "short circuit"
c3 = "G electric"
c4 = "generator"

c3 or c4

low and good and electric
c1 and (not c2) and (c3 or c4)

##########################################

7. fotmatting string (fatr)
   - f => filled character(space)
   - a => alignment (<  ^  > )
   - t => total character count
   - r => round
   
   - f keyword , {}, colon =>  f"BMW-{n:fat.2f}"


1  =>  "BMW-00001"
2  =>  "BMW-00002"
70 =>  "BMW-00070"

f = 0
a = >   
t = 5

round
0.6666  => .0f => 1
0.6666  => .1f => 0.7
0.6666  => .2f => 0.67

####################################################################################
####################################################################################

3. Loop
   1. Iteration - value     
   2. Looping - 12 times
   3. nested loop
   4. definite loop (for)
   5. indefinite loop (while)
   6. break => to stop loop
   
##########################################

1. Iteration

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]     13 

for number in numbers:
    print(f"2 x {number} = {2 * number}")

for r in range(1, 13, 1):
    print(f"2 x {r} = {2 * r}")

##########################################

2. Looping - 12 times   (definite loop)

for _ in range(12):
    print("apple")

##########################################

3. nested loop

print("2 x 1 = 1")

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
2 x 11 = 22
2 x 12 = 24

for r in range(1, 13, 1):
    print(f"2 x {r} = {2 * r}")

print('-' * 42)

##########################################

for r in range(1, 13, 1):
    print(f"2 x {r} = {2 * r}")

print('-' * 42)

for r in range(1, 13, 1):
    print(f"3 x {r} = {3 * r}")

print('-' * 42)

for r in range(1, 13, 1):
    print(f"4 x {r} = {4 * r}")

print('-' * 42)

for r in range(1, 13, 1):
    print(f"5 x {r} = {5 * r}")

print('-' * 42)

for r in range(1, 13, 1):
    print(f"6 x {r} = {6 * r}")

print('-' * 42)

....

....

##########################################

for l in range(2, 17, 1):
    for r in range(1, 13, 1):
        print(f"{l} x {r} = {l * r}")
    print('-' * 42)
    
####################################################################################

5. indefinite loop (while)

condition = True

while condition:

    user_name = input("user name = ")
    password = input("password = ")

    if user_name == "abc" and password == "12345":
        print("login successful.(opened abc' account.)")
        condition = False

    else:
        print("Wrong password. Try again.")

    print('-' * 42)


##########################################

while True:

    user_name = input("user name = ")
    password = input("password = ")

    if user_name == "abc" and password == "12345":
        print("login successful.(opened abc' account.)")
        break

    else:
        print("Wrong password. Try again.")

    print('-' * 42)

##########################################

n = 0

while True:

    user_name = input("user name = ")
    password = input("password = ")

    if user_name == "abc" and password == "12345":
        print("login successful.(opened abc' account.)")
        break

    else:
        print("Wrong password. Try again.")
        n += 1
        if n == 3:
            print("Wait 24 hours.")
            break

    print('-' * 42)
    
##########################################

condition = True
n = 0

while condition:
    user_name = input("user name = ")
    password = input("password = ")

    if user_name == "abc" and password == "12345":
        print("login successful.(opened abc' account.)")
        condition = False

    else:
        print("Wrong password. Try again.")
        n += 1
        if n == 3:
            print("Wait 24 hours.")
            break

    print('-' * 42)

else:
    print("rurdyjyjdyr")
    
####################################################################################
####################################################################################

4. Function
   - code reuse

   1. call, invoke   => ( )

##########################################

Step.1


def m2():
    for r in range(1, 13, 1):
        print(f"2 x {r} = {2 * r}")
    print('-' * 42)


def m3():
    for r in range(1, 13, 1):
        print(f"3 x {r} = {3 * r}")
    print('-' * 42)


def m4():
    for r in range(1, 13, 1):
        print(f"4 x {r} = {4 * r}")
    print('-' * 42)
       
    
m2()
m3()
m4()

##########################################

Step.2


def m(l):
    for r in range(1, 13, 1):
        print(f"{l} x {r} = {l * r}")
    print('-' * 42)
    
    
m(2)
m(3)
m(4)

##########################################

Step.3


def m(l):
    for r in range(1, 13, 1):
        print(f"{l} x {r} = {l * r}")
    print('-' * 42)


def m_10(l):
    for r in range(1, 11, 1):
        print(f"{l} x {r} = {l * r}")
    print('-' * 42)


m(l=16)
m_10(l=16)

##########################################

Step.4

def m(l, n):
    for r in range(1, n+1, 1):
        print(f"{l} x {r} = {l * r}")
    print('-' * 42)


m(l=16, n=12)
m(l=16, n=10)

####################################################################################

"""








