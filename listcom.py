a = [x for x in range(2, 20) if all(x % y != 0 for y in range(2, x))]

b = filter(lambda x: all(x % y != 0 for y in range(2, x)), range(2, 13))

c = [x for x in range(10) if x%2 == 0]

print b
print a
print c


print [x for x in range(2,20) if all (x%y !=  0 for y in range(2,x))]
print filter(lambda x : all (x% y != 0 for y in range(2,x)), range(2,20))