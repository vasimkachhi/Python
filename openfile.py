with open("string.py", "r") as fp:
    print fp.read()

with open("string.py", "r") as fp:
    print(fp.readlines()[10])