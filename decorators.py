def smart_add(func):
    def inner(*arg):
        print("*" * 30)
        return func(*arg)
    return inner

@smart_add
def add(*arg):
    return sum(arg)


print add(5,9,7,0)
