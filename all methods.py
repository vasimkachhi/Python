import pandas as pd
import os
import time

# read csv file
data = pd.read_csv('/home/developer2/all.csv')
# write csv
data.to_csv('/home/developer2/all.csv', index=False, sep=',')

# read simple file
d = open("/home/developer2/prepare", 'r')
data = d.read()
# write simple file
d = open('/home/developer2/jyjgj555jjygjjjghjgh', 'w')
d.write(data)
x = open("C:\Users\Vasim\Documents\python", 'r')
print x.readlines()[11]
import pymongo
obj = pymongo.MongoClient('192.168.5.187')
mon = obj.Universe.MacroHistData
data = mon.find().limit(10)
print pd.DataFrame(list(data))

import MySQLdb
obj= MySQLdb.connect("192.168.5.6",'mysqlusr','mysql1','Apollo')
cur = obj.cursor()
cur.execute('SElect * from Alert')
data = cur.fetchall()
desc = cur.description
result = []
for row in data:
    doc = {}
    for name, value in zip(desc, row):
        doc[name[0]] = value
    result.append(doc)
print pd.DataFrame(list(data))
#
# #List
#
test = [1,9,7,5,3,4,6,9,7]
print test
test.remove(9)
test.remove(9)
print test
a = ['vasim','kachhi']
print len(test)
print sum(test)
print test[:]
print test[::-1]
print test[::2]
print sorted(test)
print 'a' in test
print test.count(9)
print test + a
test.append(a)
print test
test.extend(a)
print test
a = test
a.append('junk')
print a
print test
test.insert(len(test)-5,788)
print test
print test.index(788)

# dictionary

test= {'name':'Vasim', 'surname':"kachhi", 'phone':9096720223}
test1= {'name':'Vasim', 'surname':"kachhi"}
print test
print test.keys()
print test.values()
print cmp(test1, test)
a = test.fromkeys([5,6,9],9)
print a
print test.has_key('name')
print test.items()
print test.get('name', 'vk')
print test.get('name1', 'vk')
test.setdefault('phone',9096)
print test
test.update({"qua":'Be'})
print test

import math
print round(9.94812354,5)
print math.floor(9.9569566)
print math.ceil(9.9569566)
print abs(-9565646132)

#string
test = "MynameisVasim"
print test.center(40,' ')
print test.isalnum()
print test.isalpha()

# set
a = {1,2,3,4}
b ={5,6,7,8,1,2}
print a
a.add(99)
print a
a.update([98])
print a
a.discard(99)
print a
a.remove(98)
print b
print a | b
print a & b
print a - b
print a ^ b


#range
print range(1,5)
print range(0,10,2)
print range(10,-1,-1)
a = xrange(1,5)
for i in a:
    print i

# Linux terminal

print os.system('ls -l')
print os.system('ps aux| grep calculator')
print os.system('kill -9 %s' %4496)
os.mkdir('/home/developer2/vkachh')
os.system('mkdir /home/developer2/vkachh')
os.rename('/home/developer2/tat.csv', '/home/developer2/TAT.csv')
os.remove('/home/developer2/TAT.csv')
os.chdir("/home/developer2/")
print os.system('ls')
os.system('vim /home/developer2/TAT.txt')
print os.path.exists('/home/developer2/tat.csv')
fd= os.mknod('/home/developer2/tat')
fd = os.open("/home/developer2/tat", os.O_RDWR|os.O_CREAT)
os.write(fd, 'This is awesome!')
os.rmdir('/home/developer2/vkachh')
print os.system("find '/home' -name jan.pdf")
print os.system('ls')

# time
print time.asctime(time.localtime(time.time()))
print time.asctime(time.strptime("2016-05-27",'%Y-%m-%d'))
a = time.get
print time.strftime('%Y-%m-%d',time.gmtime(time.mktime(2016,05,27)))


# lambda funtions
a = lambda x, y: x**2 + y
print a(9, 8)
def mak(h):
    return lambda x:x+h
a = mak(2)
print a(9)

# map funtions
print map(lambda x : x+2,[2,4,6,8])
print map(lambda x,y : x+y,[1,2,3,4,5],[6,7,8,9,0])

# filter funtions
def test(x):
    if x%7 ==0:
        return x
print filter(test, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# reduce
print reduce(lambda x, y: x + y, [2, 6, 8])
print reduce(lambda a, b : a if a > b else b, [47, 99, 66, 44])
print reduce(lambda a, b : a if a < b else b, [47, 99, 66, 44])

# decorators



def decorate_me(func):
    def inner(a, b):
        print "In Decorator"
        if b == 0:
            print "Opps..! can not devide by 0, So replaced 0 by 1.Go ahead.."
            b = 1
        return func(a, b)
    return inner


@ decorate_me
def func(a, b):
    return a / b

print func(8, 0)

print func(8, 2)

def decorate_me(func):
    print "In Decorator"
    return func


@ decorate_me
def func():
    print "Main function"

print func()


# clouser

def clouser_example(mesg):
    def inner(a):
        print mesg
a = clouser_example("Clouser example")
print a
a()

def clouser_example(mesg):
    def inner(aa):
        print mesg + aa
    return inner
a = clouser_example("Clouser example")
print a
a("By PPPK")

# iterator
# for loop in python internal processing
list = [9, 5, 1, 3]
my_list = iter(list)
while True:
    try:
        element = next(my_list)
        print element,
    except StopIteration as st:
        break

# generator

b = [x*x for x in range(1,10)]
a = (x*x for x in range(1,10))
print a
print b
print next(a)
print next(a)


def my_generator(i):
    h = i
    print (h)
    yield h
    h += 1
    print (h)
    yield h
    h += 1
    print h
    yield h
a = my_generator(1)
print a
next(a)
next(a)
next(a)
next(a)

def rev(str):
    lene = len(str)
    print range(lene-1,-1,-1)
    for i in range(lene-1,-1,-1):
        yield str[i]
for char in rev("Vasim"):
    print char
a = rev("VASIM")
print a
print next(a)



def printinfo( arg1, *vartuple ):
    "This prints a variable passed arguments"
    print "Output is: "
    print arg1
    for var in vartuple:
        print var
    return

# Now you can call printinfo function
printinfo(10)
printinfo(70, 60, 50, 88, 99)


def printinfo( *arg1):
    "This prints a variable passed arguments"
    print arg1
    for var in arg1:
        print var
    return

# Now you can call printinfo function
printinfo(10)
printinfo(10, 50, 90, 70)
printinfo(70, 60, 50, 88, 99)



def printinfo( **kwargs):
    "This prints a variable passed arguments"
    print kwargs
    for name, var in kwargs.items():
        print name, var
    return

# Now you can call printinfo function
printinfo(name= 'Vasim')
printinfo(name= 'Vasim', lname="Kachhi")
printinfo(name= 'Vasim', lname="Kachhi", phone=9096)
printinfo(name= 'Vasim', lname="Kachhi", phone=9096, age= 25)

from collections import Counter
import operator
a =  Counter("VAASIM")
print operator.itemgetter(1)
print (max(a.iteritems(), key= operator.itemgetter(1)))
print (a)

b = max
print pd.DataFrame([[1, 2], [1, 2], [9, 0], [999, 55]], index=['one', 'two', 'i', 'j'], columns=['three', 'four'])


