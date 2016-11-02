import glob
import os

path = 'C:\Users\Vasim\Desktop\GITHUB'
for filename in glob.glob(os.path.join(path, '*.py')):
    print filename
    dbname = os.path.splitext(os.path.basename(filename))[0]
    print dbname
    with open(filename) as fp:
        data = fp.read()
