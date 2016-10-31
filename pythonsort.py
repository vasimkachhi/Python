# Single swap
def testswap(a):
    b = sorted(a)
    count = 0
    for i in range(0, len(a)):
        if a[i] != b[i]:
            count += 1
    if count <= 2:
        return True
    else:
        return False
print testswap([4, 3, 7, 9])


# element and index
z = [1, 8, 9, 3, 1, 6, 9, 2]
count = 0
for i in range(0, len(z)):
    for j in range(i+1, len(z)):
        if z[i] == z[j]:
            count += 1
print count

# pivot element
for i in range(0, len(z)):
    if sum(z[:i]) == sum(z[i+1:]):
        print z[i]
        print sum(z[:i]), sum(z[i+1:])

# sort list without inbuilt function
for i in range(len(z)):
    for j in range(len(z) - 1):
        if z[j] > z[j+1]:
            t = z[j]
            z[j] = z[j+1]
            z[j+1] = t
print z

# string
def strpalind(x):
    y = x[::-1]
    if x.lower() == y.lower():
        return True
    else:
        return False
strpalind("bbB")


# int palindrome
def numpalin(x):
    y = x
    a = 0
    while y != 0:
       a = y % 10 + a * 10
       y = y / 10
    if a == x:
        print("Is plalindrome")
    else:
        print("Not a palindromw")
numpalin(787)

# max length palindrome
import operator
import collections
a = "my name in Vasim BBBBB Eeeeee EEEEEEEEEEeeeeeeeeEE"
l = a.split(" ")
pal = filter(strpalind, l)
t ={x: len(x) for x in pal}
print (max(t.iteritems(), key=operator.itemgetter(1)))


import re
z = "9my name in Vasim BBBBB Eeeeee EE]EEEEEEEEeeeeeeee,,,,,.../../.EE"
print re.sub('[^a-zA-Z0-9 ]','', z)


c= "vasims2"
print ''.join(reversed(c))

print c.isalnum()
print c.isalpha()
print c.isdigit()