#un=input('plz enter ur name = ')
#pwd=input('plz entire ur pwd = ')
#sec = '*' 
#sec1 = sec * len(pwd)
#print(f'\nhi {un}, your password is {"*" * len(pwd)} having length {len(pwd)}#')


#name  = False
#msg = 'allowed' if name else 'not'
#print(msg)

#magic=False
#exp=False
#if magic and exp:
#  print('gud expert')
#elif magic or exp:
#  print('gud enough')
#elif not(magic):
#  print('need to learn')
#else:
#  print('all are false')

#my_l=[1,2,3,4,5,6,7,8,9,10]
#j = 0
#for i in my_l[::-1]:
#  print(i)
#  j += i
#print('sum of list',j)

#for i,item in enumerate(list(range(100))):
 # if item==50:
  #  print('the index of 50 is ',i)

#picture = [ [0,0,0,1,0,0,0], [0,0,1,1,1,0,0], [0,1,1,1,1,1,0], [1,1,1,1,1,1,#1], [0,0,0,1,0,0,0], [0,0,0,1,0,0,0]]
#i,j = 0,0
#for i in picture:
#  for j in i:
 #   if j == 1:
  #    print('*', end='')
   # else:
    #  print(' ',end='') 
  #print('')
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
dup =[]
for value in some_list:
  if some_list.count(value) > 1:
    if value not in dup:
      dup.append(value)
print('dupicate in list is =',dup)

#def dr():
#  age = int(input('wats ur age? '))
  #if age < 18:
 #   print('need to wait for some more yrs')
 # elif age >= 18:
#    print('greate u r approved')
 # else:
 #   print('wait')

#dr()


high = []
def high_even(args):
  for values in args:
    if values % 2 == 0:
      high.append(values)
  return max(high)
print('highest even number is ',high_even([10,4,12,8,9,11]))



class Cat:
  Species = 'mammal'
  def __init__(self,name,age):
    self.name = name
    self.age = age

cat1 = object.Cat('tom', 10)
cat2 = object.Cat('tommy', 8)
cat3 = object.Cat('jammy', 7)

class Cat:
  Species = 'mammal'
  def __init__(self,name,age):
    self.name = name
    self.age = age
  
  def high_age(self):
    if self.age == 12:
      print(f'high age cat is {self.name} and age is {self.age}')
      return True

cat1 = Cat('tom', 10)
cat2 = Cat('tommy', 8)
cat3 = Cat('jammy', 12)

print(cat1.high_age())
print(cat2.high_age())
print(cat3.high_age())


class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#1 Add nother Cat
class Tom(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [Simon('simon', 10),Sally('Sally', 3),Tom('Tom', 12)]

#3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)

#4 Output all of the cats walking using the my_pets instance
my_pets.walk()



class SuperList(list):
    def __len__(self):
     return 1000
SL = SuperList();

SL.append(1)
SL.append(2)
SL.append(3)
print(SL)
print(SL[1])
print(len(SL))
#print(len(super_list1)

def even(list):
  if(list % 2 == 0): return list

print(list(filter(even, range(0,50))))




from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
def cap(item):
  return (item.capitalize())

print(list(map(cap, my_pets)))



#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
my_numbers.sort()
print(list(zip(my_numbers, my_strings)))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
def fil(list):
  for i in range(list):
    if i >= 50:
      return scores
print(list(filter(fil, scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def accu(acc, item):
  print(acc, item)
  return acc + item

new_num = my_numbers + scores
print(new_num)
print(reduce(accu, new_num, 0))




my_list=[5,3,2]

print(list(map(lambda item: item**2, my_list)))

a = [(0, 2), (5, 2), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])

print(a)



some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list({x for x in some_list if some_list.count(x) > 1})

print(duplicates)



# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
  def auth(*args, **kwargs):
    if args[0] ['valid']:
      print(args[0])
      print('*********')
      fn(*args, **kwargs)
      print('*********')
    return fn
  return auth

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)





# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
  def auth(*args, **kwargs):
    if args[0] ['valid']:
      print(args[0])
      print('*********')
      fn(*args, **kwargs)
      print('*********')
    return fn
  return auth

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)



def fib(number):
  a = 0
  b = 1
  for i in range(number):
    yield a
    temp = a
    a = b
    b = a + temp
  #return fib(number)
 

for x in fib(21):
  print(x)
 m-aa = 2

a.strip



print(*(i for i in range (2000 ,3002) if i%7==0 and i%5!=0 ),sep = ',')


c=int(input('enter a value for fact='))
fact = 1
i = 1
for i in range(1, c+1):
  fact = fact * i
  print(fact)

a=0
b=1
for i in range(5):
  temp=a
  a=b
  b=a+temp
  print(temp)
    
	

import random
a = random.randint(1,10)
while True:
    b = int(input("enter a random number from 1-10 = "))
    print('random number is ', a)
    print('input number is ', b)
    if a==b:
        print('your guess is correct')
    continue



a = input("enter csv numbers = ").split( ',', )
b = list(a)
c = tuple(a)
print(c)
print(b)



class Test:
    def getstring(self):
        self.a = input("type anything")
    def printstring(self):
        print(self.a)

c = Test()
c.getstring()
c.printstring()



from math import sqrt
a = input("enter").split(",")
c = []
for i in a:
    b= round(int(sqrt((2*50*int(i))/30)))
    c.append(b)
print(c)


x,y=map(int, input("enter").split(","))
l=[]
for i in range(x):
    t=[]
    for j in range(y):
        t.append(i*j)
    l.append(t)
print(l)


x,y=map(int, input("enter").split(","))
l=[]
for i in range(x):
    t=[]
    for j in range(y):
        t.append(i*j)
    l.append(t)
print(l)


a= input("enter").split(",")
a.sort()
print(a)


a = []
while True:
    s = input()
    if s:
        a.append(s.upper())
    else:
        break

for i in a:
    print(i)
	
my_set=set(input("enter some text").split(" "))
print(str(sorted(my_set)))


#0100,0011,1010,1001

my_list=input("enter value").split(",")
print(my_list)
divided=[]
for i in my_list:
    intp = int(i,2)
    if not intp%5:
        divided.append(i)
print(divided)



for i in range(1000,3001):
    if i%2==0:
        my_divided=[]
        my_divided.append(i)
    print(my_divided)


from itertools import count
my_text=input("enter the text= ")
letter,digit=0,0
for i in my_text:
    if ('a'<=i and i<='z') or ('A'<=i and i<='Z'):
        letter += 1
    else:
        digit += 1
print(letter)
print(digit)


from translate import Translator
translator = Translator(to_lang="ja")
with open("trans.txt", mode='r') as my_file:
    text=my_file.read()
    translation = translator.translate(text)
    with open("trans.txt", mode='w') as my_file2:
        my_file2.write(translation)
my_str=input("enter a string= ")
l,u=0,0
for i in my_str:
    if ('a'<=i and i<='z'):
        l +=1
    elif ('A'<=i and i<='Z'):
        u +=1
    else:
        pass
print("lower=",l,"\n upper=", u)


a=9
tmp=str()
tot=0
for i in range(4):
    tmp+=str(a)
    tot+=int(tmp)
print("total= ",tot)


import re
pattern= re.compile(r"([a-zA-Z0-9$%#@]{8,}\d)")
text="sA$%#@123assd"
print(len(text))
if len(text)>7:
    a=pattern.fullmatch(text)
    print(a)
else:
    print("@least 8 char is required")
	


my_list=input("enter some numbers= ").split(",")
n=[]
for i in my_list:
    if int(i)%2!=0:
        a=int(i)*int(i)
        n.append(a)
print("list is ", n)



Deb=[]
wit=[]
try:
    while True:
        D=int(input("enter deposit="))#.split("\n")
        Deb.append(D)
        W=int(input("enter withdraw="))#.split("\n")
        wit.append(W)
        if (not D) and (not W):
            Deb.pop()
            wit.pop()

            break
except ValueError:
    pass
print("balance amount=",sum(Deb)-sum(wit))



import unittest
import main

class Testmain(unittest.TestCase):
  def test_do_stuff(self):
    number=0
    result=main.do_stuff(number)
    self.assertEquals(result, 0)

unittest.main()


def do_stuff(num=1):
  print(num+5)
  return num+5
  
  
  
import re
password = re.compile(r"([a-zA-Z0-9$#@]{6,12})")
user_pwd = ['ABd1234@1','a F1#','2w3E*','2We3345']
for i in range(len(user_pwd)):
    a=password.fullmatch(user_pwd[i])
    print(a)

from operator import itemgetter

l = []
while True:
    s = input("enter csv=")
    if not s:
        break
    l.append(tuple(s.split(",")))

print(sorted(l, key=itemgetter(0,1,2)))




my_divisible=int(input("enter a divident="))
l=[]
for i in range(0,100):
    if i%my_divisible==0:

        l.append(i)
    #yield i
print(l)


from math import sqrt
lst = []
position = [0,0]
while True:
    a = input()
    if not a:
        break
    lst.append(a)
    print(lst)
for i in lst:
    if 'UP' in i:
        position[0] -= int(i.strip('UP '))
        print(position)
    if 'DOWN' in i:
        position[0] += int(i.strip('DOWN '))
        print(position)
    if 'LEFT' in i:
        position[1] -= int(i.strip('LEFT '))
        print(position)
    if 'RIGHT' in i:
        position[1] += int(i.strip('RIGHT '))
        print(position)
print(round(sqrt(position[1] ** 2 + position[0] ** 2)))



my_input=input("enter some test=").split()
sorty= sorted(my_input)
print(sorty)
for i in sorty:
    print("{0}:{1}".format(i, sorty.count(i)))
    #print("{0}:{1}".format(i, ss.count(i)))
    


import sys
import os
from PIL import Image
input_folder = sys.argv[1]
output_folder = sys.argv[2]
if not os.path.exists(output_folder):
    os.mkdir(output_folder)
for filename in os.listdir(input_folder):
    img = Image.open(f"{input_folder}{filename}")
    clean_name=os.path.splitext(filename)[0]
    img.save(f"{output_folder}{clean_name}.png", "png")
    print("done")
def squareroot(num, pow):
    return num**pow
print(squareroot(5,5))



def sum(a,b):
    return a+b
print(sum(5,9))


def convert(a):
    b = str(a)
    print(type(b))
    return b

print(convert(5))


def convert(a, b):
    c = int(a) + int(b)
    print(type(c))
    return c

print(convert('5','11'))


def convert(a, b):
    c = a+b
    print(type(c))
    return c

print(convert('ass','whole'))

def printValue(s1,s2):
    if len(s1) > len(s2):
         print(s1)
    elif len(s2) > len(s1):
        print(s2)
    else:
        print(s1,s2)
printValue("oneee","three")

d=dict()
for i in range(1,21):
    d[i]=i**2
print(d)

d=dict()
for i in range(1,21):
    d[i]=i**2
print(d.keys())

d=[]
for i in range(1,21):
    d.append(i**2)
print(d[:5])

d=[]
for i in range(1,21):
    d.append(i**2)
print(d[-5:])

d=[]
for i in range(1,21):
    d.append(i**2)
print(d[5:])


d=[]
for i in range(1,21):
    d.append(i**2)
c= tuple(d)
print(c, 'and' ,type(c))


my_tup=(1,2,3,4,5,6,7,8,9,10)
print(my_tup[:int(len(my_tup)/2)])
print(my_tup[int(len(my_tup)/2):])


my_tup=(1,2,3,4,5,6,7,8,9,10)
new_tup= tuple(i for i in my_tup if i%2==0)

print(new_tup)

my_in=str(input("enter a string= "))
if my_in == 'YES' or my_in == 'Yes' or my_in == 'yes':
    print(my_in)
else:
    print('No')
	
	
li = [1,2,3,4,5,6,7,8,9,10]
squaredNumbers = list(map(lambda x: x**2, li))
print(squaredNumbers)
new_li=[]
for i in li:
    new_li.append(i**2)
print(new_li)


li=[1,2,3,4,5,6,7,8,9,10]
new_li = list(map(lambda x: x**2, filter(lambda x: x%2==0, li)))
print(new_li)


evenNumbers = list(filter(lambda x: x%2==0, range(1,21)))
print(evenNumbers)


my_l=list(map(lambda x: x**2, range(1,21)))
print(my_l)

class American(object):
    @staticmethod
    def printNationality():
        print("America")

class NewYork(American):
    @staticmethod
    def printNationality1():
        print("Newyork")
anAmerican = American()
anAmerican.printNationality()
NewYork.printNationality1()

class Circle(object):
    def __init__(self, r):
        self.radius = r
    def area(self):
        return ("area of the circle", 3.14*self.radius**2)

Cir=Circle(5)
print(Cir.area())

class Rect(object):
    def __init__(self, l, b):
        self.length = l
        self.breadth = b
    def area(self):
        return self.length*self.breadth

Cir=Rect(5,5)
print(Cir.area())

class Shape(object):
    def __init__(self, l):
        self.length = l

    def area(self):
        return 0

class Square(Shape):
    def area(self):
        return ("area =",self.length*self.length)

Cir=Square(5)
print(Cir.area())


raise RuntimeError('something wrong')

def divide():
    return 5/0
try:
    divide()
except ZeroDivisionError as err:
    print("caught the error")
except:
    print("Any other exception")
	
	
	
class CustomException(Exception):
    """Exception raised for custom purpose

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


num = int(input())

try:
    if num < 10:
        raise CustomException("Input is less than 10")
    elif num > 10:
        raise CustomException("Input is grater than 10")
except CustomException as ce:
    print("The error raised: " + ce.message)


import re

pattern= re.compile(r"([a-zA-Z]+)\@([a-zA-Z\.]+)")
mail_id= input("enter a email id=")
print(pattern.fullmatch(mail_id).group(1))



my_in=input("enter the strng=").split()
new_li=[]
for i in my_in:
    print(i)
    if not ('a'<=i and i<='z') or ('A'<=i and i<='Z'):
        new_li.append(i)
print(new_li)

import re
s = input()
print(re.findall("\d+",s))


s = "hellooooo"
u = s.encode('utf-8')
print(u)


my_in=int(input("enter a number="))
new=[]
for i in range(1,my_in+1):
    print(i)
    new.append(i/(i+1))
print(sum(new))




def f(n):
    if n==0:
        return 0
    else:
        return f(n-1)+100


n=int(input())
print(f(n))


def f(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n>1:
        return f(n-1)+f(n-2)
    else:
        return ("provide +ve int")
n=int(input("enter an int="))
print(f(n))


def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(input("enter"))
for x in range(0, n+1):
    values = [str(f(x))]
    print(",".join(values))
	
	
# Solution by: StartZer0
n = int(input("enter="))

for i in range(0, n+1, 2):
  if i < n - 1:
    print(i, end = ',' )
  else:
   print(i)
   
# Solution by: StartZer0
n = int(input("enter="))
for i in range(0, n):
  if (i%35==0):
      print(i, end=',')

list=[2,4,6,8,11]
for i in list:
    assert i%2==0


i=input("enter=")
print("result=",eval(i))

import random

print(random.random()*100)


import random

print(random.uniform(5,95))


import random

li=[]
for i in range(10,151,35):
    li.append(i)
print(li)
print(random.choice(li))

import random

li=[]
for i in range(0,11,2):
    li.append(i)
print(li)
print(random.choice(li))


import random

li=[]
for i in range(100,201):
    li.append(i)
print(li)
print(random.sample(li,5))

import random

li=[]
for i in range(100,201, 2):
    li.append(i)
print(li)
print(random.sample(li, 5))

import random

li=[]
for i in range(1,1000, 35):
    li.append(i)
print(li)
print(random.sample(li, 5))

import random

print(random.randrange(7,15))




import zlib
s = 'hello world!hello world!hello world!hello world!'
# In Python 3 zlib.compress() accepts only DataType <bytes>
y = bytes(s, 'utf-8')
x = zlib.compress(y)
print(x)
print(zlib.decompress(x))


from timeit import Timer
t = Timer("for i in range(100):1+1")
print(t.timeit())



from random import shuffle as shu
li=[2,4,5,6,8]
shu(li)
print(li)



subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            sentence = "%s %s %s." % (subjects[i], verbs[j], objects[k])
            print(sentence)
			


li=[5,6,77,45,22,24,12]
li=[x for x in li if x%2!=0]
print(li)


li=[12,24,35,70,88,120,155]
li=[x for x in li if x%35!=0]
print(li)


li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i%2 != 0 and i <= 6]
print(li)


li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i<3 or 4<i]
print(li)


array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
print('\n',array)


li=[12,24,35,70,88,120,155]
li=[x for (i,x) in enumerate(li) if i not in (0,4,5)]
print(li)

li=[12,24,35,70,88,120,155]
li=[i for i in li if i!=24 ]
print(li)

a,b=[1,3,6,78,35,55],[12,24,35,24,88,120,155]
c=a+b
print(c)


set1=set([1,3,6,78,35,55])
set2=set([12,24,35,24,88,120,155])
set1 &= set2
print(set1)
li=list(set1)
print(li)

li=[12,24,35,24,88,120,155,88,120,155]
a =set(li)
print(sorted(a, reverse=True))


class Person(object):
    def __init__(self):
        self.gender="unknown"
    def getgender(self):
        print(self.gender)

class Male(Person):
    def __init__(self):
        self.gender="Male"

class Female(Person):

    def __init__(self):
        self.gender="Women"
M=Male()
f=Female()
M.getgender()
f.getgender()


s = input("enter=")
for i in sorted(set(s)):
    print(f'{i}, {s.count(i)}')
	

li=input("enter=")
s=li[::-1]
print(s)

s=input("enter")
s=s[::2]
print(s)


import itertools
print (list(itertools.permutations([1,2,3])))



n = int(input("enter score="))
arr = map(int, input().split())
arr = list(set(arr))
arr.sort()
print("runner up is",arr[-2])


import textwrap

string = input("enter a str=")
width = int(input("enter a number="))
print(textwrap.fill(string,width))


import calendar
mon, day, yr =map(int, input("enter a date=").split())
print(calendar.day_name[calendar.weekday(yr, mon, day)])


if __name__ == '__main__':
    n = int(input("enter="))
    set1 = set(map(int,input().split()))

    m = int(input('enter='))
    set2 = set(map(int, input().split()))

    ans = list(set1 ^ set2)
    ans.sort()
    for i in ans:
        print(i)
		
		
li=input("enter=")
d,a=0,0
for i in li:
    d +=i.isdigit()
    a +=i.isalpha()
print(f'\n digit={d} alpha={a}')


li=int(input("enter="))
sum=0
for i in range(li+1):
    sum +=i
print(f'\n sum={sum}')



def rec(n):
    if n == 0:
        return n
    return rec(n-1) + n


n = int(input())
sum = rec(n)
print(sum)