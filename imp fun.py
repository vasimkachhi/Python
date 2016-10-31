a = 'sdfdfdfdfgfdfgffsdcccccccc'
b = {}

for i in a:
    try:
        b.update({i: b[i] +1})
    except Exception as e:
        b.update({i: 1})
new = {}

print {name: value for name,value in b.iteritems() if value == max(b.values())}
exit()
for name,value in b.iteritems():
    if value == max(b.values()):
      new.update({name:value})
print new

for i in range(1, 31):
    if (i % 3 == 0) & (i % 5 == 0):
        print "both",
    elif i % 5 == 0:
        print "5",
    elif i % 3 ==0:
        print "3",
    else:
        print i,
