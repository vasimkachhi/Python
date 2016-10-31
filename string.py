import re

def check_pal(stri):
    revstr = stri[::-1]
    status = False
    if revstr == stri:
        status = True
    return status

b = "my name is vasim, and i am be graduate in Computers mmmmmmmmmm bb bfb aaaaaaaa dd d,./'3ddd[]"
a = re.sub('[^A-Za-z0-9 ]', '', b)
a = a.split(" ")
a = filter(check_pal, a)
print max(a, key=len)
print max(filter(check_pal, re.sub('[^A-Za-z0-9 ]', '', b).split(" ")), key=len)


print max(filter(lambda x: True if x == x[::-1] else False,
                 re.sub('[^A-Za-z0-9 ]', '', raw_input("Your string \n")).split(" ")), key=len)


