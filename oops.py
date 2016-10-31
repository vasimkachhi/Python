class a:
    def met(self):
        print 'a'
class b(a):
    def met(self):
        print 'b'
class c(a):
    # pass
    def met(self):
        print 'c'

class d(c,b):
    def met(self):
        super(d,self).met()
        print 'd'
    # pass
o = d()
print type(o)
# o.met()
# super(b, o).met()



print 3/2
print 3//2

print 3/2.0
print 3//2.0
