def compare(file1,file2):
    a = open(file1)
    b = open(file2)
    count = 0
    line = 0
    result = []
    while 1:
        temp1 = a.readline()
        temp2 = b.readline()
        line +=1
        if temp1 != temp2:
            count += 1
            result.append(line)
        if temp1 == '' and temp2 == '':
            return [count,result]
            break
    a.close()
    b.close()
def get_result():
    file1 = input('请输入需要比较的头一个文件名：')
    file2 = input('请输入需要比较的另一个文件名：')
    result = compare(file1,file2)
    print('两个文件共有【%d】处不同'%result[0])
    for line in result[1]:
        print('第%d行不一样' % line)
get_result()
