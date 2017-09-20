import os
import os.path
file_catalog = input('请输入待查找的初始目录：')
a = list(os.walk(file_catalog))
b = []
for i in a:
    for i1 in i[2]:
        d = os.path.splitext(i1)
        if d[1] in ['.avi','.rmvb','.mp4']:
            t= i[0]+'\\'+ str(i1)
            b.append(t)
c = open( 'videoList.txt','x+')
for i2 in b:
    c.write('%s\n\n' % i2)
c.close()
