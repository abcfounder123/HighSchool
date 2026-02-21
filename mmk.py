
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

1. Procedural programming
2. OOP
   - Attributes
   - tightly couple, "is a"     - hand, engine   <= inheritance
   - loosely couple, "has a"    - clothes, tire  <= composition

Object-oriented Programming

- a paradigm based on the concept of "objects"
- paradigm ဂရိစကားလုံး တွေးပုံတွေးနည်း
- concept အယူအဆ / အမြင်
- object  အရာဝတ္ထု

အရာဝတ္ထုဆိုတဲ့ အယူအဆအပေါ်မှာ အခြေခံထားတဲ့ တွေးပုံတွေးနည်း ဖြစ်ပါတယ်။

အရာဝတ္ထုလို့တွေးပြီး program ရေးတာ ဖြစ်ပါတယ်။

##################################################

Attributes exercises

အရာဝတ္ထုတွေမှာ ကိုယ်ပိုင် ပိုင်ဆိုင်မှုတွေ ရှိကြပါတယ်။

ဒီနေ့သင်ခန်းစာက ပိုင်ဆိုင်မှုနဲ့ပတ်သတ်ပြီး စနစ်တကျ တွေးတတ်ဖို့ ဖြစ်ပါတယ်။

အဆင့်ဆယ်ဆင့်ရှိပြီး ပထမနှစ်ဆင့်ကို လေ့ကျင့်ပြီး အသားကျမှသာ ကျန်တာတွေ ဆက်လေ့လာလို့ရပါမယ်။

##################################################

1. Write

ပထမအဆင့်ကတော့ အတွေးတွေကို ချရေးတာ ဖြစ်ပါတယ်။

အများကြီးနဲ့ ရှုတ်ရှုတ်ထွေးထွေး မတွေးပဲ နည်းနည်းလေးနဲ့ ရိုးရိုးလေးပဲ တွေးရပါမယ်။

ရိုးရိုးလေးတွေးပြီး ရေးတတ်စေချင်တာပါ။


##################################################

2. Divide (data, fun/method)

ဒုတိယအဆင့်ကတော့ ရေးထားတာကို ခွဲထုတ်တာ ဖြစ်ပါတယ်။

ခွဲထုတ်တဲ့အချိန်မှာ အတွေးတွေကို ဖျောက်ထားရမှာဖြစ်ပြီး အသစ်ထပ်ထည့်တာတွေ မလုပ်ရပါဘူး။

ရေးထားတဲ့အတိုင်းဖတ်ပြီး စက်ရုပ်လိုမျိုး ခွဲထုတ်ပေးရပါမယ်။

ခွဲထုတ်ရင်းနဲ့ data ဘယ်နှစ်ခု၊ function ဘယ်နှစ်ခု စသဖြင့် အရေအတွက်အပါအဝင် ပေးထားတဲ့အမည်တွေနဲ့ အလုပ်လုပ်ပုံတွေကိုပါ တစ်ခါတည်း အလွတ်ရအောင် မှတ်ထားဖို့လည်း လိုအပ်ပါသေးတယ်။

မှန်မှန်ကန်ကန် ခွဲထုတ်တတ်ဖို့နဲ့ မှတ်တတ်တဲ့အကျင့် ရှိစေချင်တာပါ။

##################################################

Python ၏ အနှစ်သာရ

1. လှတာ ပိုကောင်းတယ်။

2. ရှင်းလင်းတာ ပိုကောင်းတယ်။

3. အတွေးတွေဟာ ရိုးရှင်းနေရမယ်။

###################################################################################################

Object-oriented Programming

- a paradigm based on the concept of "objects"

#################################################

Attributes exercises

Step.1   --->   Write

7. Car မှာ ကားနံပါတ် တာယာနဲ့ အင်ဂျင်ပါတယ်။ (VIN, tires, engine)
class   ---> Car
data    ---> VIN, tires, engine
method  ---> download(self)

8. Tires ( ကားတာယာ ) တွင် size နှင့် pressure ပါသည်။
pressure ၏ မူလတန်ဖိုးသည် 0 ( psi ) ဖြစ်သည်။
လေထိုးသောလုပ်ဆောင်ချက်ပါသည်။ သတ်မှတ်ပေးလိုက်သော ဖိအားအတိုင်း လေထိုးပေးမည်။

9. Engine တွင် fuel_type ပါသည်။
စက်နှိုး/မနှိုး ဟူသော အခြေအနေ  state ပါသည်။
မူလအခြေအနေမှာ စက်မနှိုးထားသဖြင့် off ဖြစ်နေမည်။
ပေးထားသော fuel_type ဖြင့် စက်နှိုး ၊ စက်ရပ် မည့်လုပ်‌ဆောင်ချက်ပါသည်။ ( on(), off() )

###################################################################################################

Step.2   --->   Divide

class   --->
data    --->
method  --->

7. Car မှာ ကားနံပါတ် တာယာနဲ့ အင်ဂျင်ပါတယ်။ (VIN, tires, engine)
class   --->  Car
data    --->  VIN, tires, engine
method  --->

8. Tires ( ကားတာယာ ) တွင် size နှင့် pressure ပါသည်။
pressure ၏ မူလတန်ဖိုးသည် 0 ( psi ) ဖြစ်သည်။
လေထိုးသောလုပ်ဆောင်ချက်ပါသည်။ သတ်မှတ်ပေးလိုက်သော ဖိအားအတိုင်း လေထိုးပေးမည်။
class   --->  Tires
data    --->  size, pressure = 0
method  --->  pump(p)

def pump():
    print(f"pump to 0 psi.")


def pump(p):
    print(f"pump to {p} psi.")


9. Engine တွင် fuel_type ပါသည်။
စက်နှိုး/မနှိုး ဟူသော အခြေအနေ  state ပါသည်။
မူလအခြေအနေမှာ စက်မနှိုးထားသဖြင့် off ဖြစ်နေမည်။
ပေးထားသော fuel_type ဖြင့် စက်နှိုး ၊ စက်ရပ် မည့်လုပ်‌ဆောင်ချက်ပါသည်။ ( on(), off() )
class   --->  Engine
data    --->  fuel_type, state = "off"
method  --->  on(), off()

###################################################################################################

Car မှာ ကားနံပါတ် တာယာနဲ့ အင်ဂျင်ပါတယ်။ (VIN, tires, engine)
Tires ( ကားတာယာ ) တွင် size နှင့် pressure ပါသည်။
pressure ၏ မူလတန်ဖိုးသည် 0 ( psi ) ဖြစ်သည်။
လေထိုးသောလုပ်ဆောင်ချက်ပါသည်။ သတ်မှတ်ပေးလိုက်သော ဖိအားအတိုင်း လေထိုးပေးမည်။
Engine တွင် fuel_type ပါသည်။
စက်နှိုး/မနှိုး ဟူသော အခြေအနေ  state ပါသည်။
မူလအခြေအနေမှာ စက်မနှိုးထားသဖြင့် off ဖြစ်နေမည်။
ပေးထားသော fuel_type ဖြင့် စက်နှိုး ၊ စက်ရပ် မည့်လုပ်‌ဆောင်ချက်ပါသည်။ ( on(), off() )

class   --->   Car
data    --->   VIN, tires, engine
method  --->

class   --->  Tires
data    --->  size, pressure = 0
method  --->  pump(p)

class   --->  Engine
data    --->  fuel_type, state = off
method  --->  on(), off()

##################################################################################################

Step.3   --->   Draw design

Prefix data or external data


class Tires:
    def __init__(self):
        self.pressure = 0         <--- prefix data


class Laptop:
    def __init__(self, x):
        self.serial_no = x       <--- external data


#################################################

Function with obj data


def download(self):
    print("Download with", self.speed)


#################################################

Function with obj data + external data 1


def pump(self, p):
    print(f"pump to {p} psi.")


#################################################


class Tire:
    def __init__(self, s):
        self.size = s
        self.pressure = 0

    def pump(self, p):
        print(f"Pump to {p} psi.")
        self.pressure = p


t1 = Tire(15)     # Mandalay  4380434 912
t2 = Tire(18)     # Yangon    4380434 864

print(id(t1))
print(id(t2))


Mandalay
Mandalay.on the table = book



4380434912
4380434864


x = Tire(15)     # Mandalay
y = x            # Mandalay

#################################################

1. House design           <---  paper                   class Tire
2. Python => Computer     <---  create                  Tire(15)
3. house1, house2         <---  Mandalay, Yangon        4298171472, 4298171520
4. Label1                 <---- Mandalay                4298171520

###################################################################################################


class Tire:
    def __init__(self, x):
        self.pressure = 0
        self.size = x

    def pump(self, p):
        print(f"pump to {p} psi.")
        self.pressure = p


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        print("Engine On.")
        self.state = "on"

    def off(self):
        print("Engine Off.")
        self.state = "off"


class Car:
    def __init__(self, VIN, tires, engine):
        self.VIN = VIN
        self.tires = tires
        self.engine = engine

##################################################################################################

Test city_car

# city_car = Car(VIN=str("BMW-0001"), tires=Tire(15), engine=Engine("petrol"))

city_car = Car("BMW-0001", Tire(15), Engine("petrol"))

print(city_car.tires.pressure)
print(city_car.engine.state)

city_car.tires.pump(7)
city_car.engine.on()

print(city_car.tires.pressure)
print(city_car.engine.state)

##################################################################################################

Step.4   --->  controlling data by function   (state <-- on(), off() )



class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        print("Engine On.")
        self.state = "on"

    def off(self):
        print("Engine Off.")
        self.state = "off"

        
##################################################################################################

Step.5   --->  controlling function by data


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        if self.state == "off":
            print("Engine On.")
            self.state = "on"
        else:
            print("Already On.")

    def off(self):
        if self.state == "on":
            print("Engine Off.")
            self.state = "off"
        else:
            print("Already Off.")
            
            
e = Engine("petrol")
e.on()
e.on()
e.on()
e.on()

##################################################################################################

Step.6   --->  representation string

<__main__.Engine object at 0x10276a6f0>
<__main__.Engine object at 0x10276a690>

petrol engine
diesel engine


def __repr__(self):
    return f"<__main__.Engine object at {hex(id(self))}>"

def __repr__(self):
    return f"{self.fuel_type} engine"

#################################################       


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "off"

    def on(self):
        if self.state == "off":
            print("Engine On.")
            self.state = "on"
        else:
            print("Already On.")

    def off(self):
        if self.state == "on":
            print("Engine Off.")
            self.state = "off"
        else:
            print("Already Off.")

    def __repr__(self):
        return f"{self.fuel_type} engine"


e = Engine("petrol")
print(e)

e2 = Engine("diesel")
print(e2)

##################################################################################################


"""








