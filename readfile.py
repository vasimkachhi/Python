import glob
import os
# only one dir
for filename in glob.glob('C:\Users\Vasim\Desktop\GITHUB\*py'):
    print filename
    dbname = os.path.splitext(os.path.basename(filename))[0]
    print dbname
    with open(filename) as fp:
        data = fp.read()

# sub directories also
import os, glob, itertools
configfiles = itertools.chain.from_iterable(glob.iglob(os.path.join(root,'*.*'))
                         for root, dirs, files in os.walk('C:\Users\Vasim\Desktop\GITHUB'))
for a in enumerate(configfiles):
    print a
