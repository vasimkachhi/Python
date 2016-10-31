a = [1,4,5,6,7,8]
b = [1,4,5,6,7,8]

x = map(lambda x,y : x+y ,[1,4,5,6,7,8],[1,4,5,6,7,8])
print x



f = filter(lambda x:x % 2 == 0,[1,4,5,6,7,8])

print f

r= reduce(lambda  x,y :x+y ,[1,4,5,6,7,8])
print r

z= [x+y for x,y in zip([1,4,5,6,7,8],[1,4,5,6,7,8])]
print z


