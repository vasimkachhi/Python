import re
print max(filter(lambda x: True if x == x[::-1] else False,
                 re.sub('[^A-Za-z0-9 ]', '', raw_input("Your string \n")).split(" ")), key=len)
