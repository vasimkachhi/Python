class test:
    """
    JUST
    """
    a = 1
    b = 3
    c = 10

    def t1(self, a):
        """
        T1
        """
        print a

    def t2(self, b):
        """
        T2
        """
        print b

if __name__ == '__main__':
    obj = test()
    print dir(obj)
    print vars(obj)
    setattr(obj, "a", "v")
    print vars(obj)
    obj.t1(obj.a)
