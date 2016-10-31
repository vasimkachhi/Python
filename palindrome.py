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