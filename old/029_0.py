def put_in_file():
    filecontent = []
    filename = input('请输入文件名：')
    a = open(filename,'w')
    while 1:
        filecontent.append(input('请输入内容【单独输入'':w''保存退出】'))
        if ':w' in filecontent:
            break
        else:
            a.writelines(filecontent)
    a.close()
put_in_file()
