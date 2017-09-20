import os
import os.path
def file_detect():
    c = {}
    file_list = os.listdir()
    for i in file_list:
        b = os.path.splitext(i)
        if b[1] in c:
            c[b[1]] +=1
        else:
            c.setdefault(b[1])
            c[b[1]]=1
    return c

a = file_detect()
for i in a:
    if i != '':
         print('该文件夹下共有类型为【%s】的文件%s个'% (i,a[i])) 
    else:
         print('该文件夹下共有类型为【%s】的文件%s个'% ('文件夹',a[i]))
