import os
import os.path

a = os.listdir()
for i in a:
    print('%s【%sBytes】'% (i,os.path.getsize(i)))
