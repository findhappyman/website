import os
import os.path
file_catalog = input('请输入待查找的初始目录：')
file_name = input('请输入需要查找的目标文件：')
a = list(os.walk(file_catalog))
for i in a :
    if file_name in i[2]:
        print('%s\\%s' % (i[0],file_name))
        
