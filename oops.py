class a(object):
    def met(self):
        print 'a'
    # pass


class b(a):
    # pass
    def met(self):
        print 'b'


class c(a):
    # pass
    def met(self):
        print 'c'


class d(c, b):
    # pass
    def met(self):
        # super(d, self).met()
        print 'd'
o = d()
print type(o)
o.met()
# super(d, o).met()



# print 3/2
# print 3//2

# print 3/2.0
# print 3//2.0
