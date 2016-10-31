

a = 1
b = 1
print a,
print b,
for i in range(8):
    print a + b,
    a , b = b, a + b

print

a = 407
l = len(str(a))
temp = a
sum = 0
while temp >0:
    digit = temp %10
    sum += digit ** l
    temp = temp /10
print sum
