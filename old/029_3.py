def print_file():
    b = []
    filename = str(input('请输入要打开的文件：'))
    while 1:
        file_line = input('请输入需要显示的行数【格式如21:23 或:12 或 21:】：')
        a = open(filename)
        for each_line in a:
            b.append(a.readline())
        if file_line == ':':
            print(b,end='')
            break
        elif ':' in file_line:
            (b1,b2)=file_line.split(sep= ':')
            print(b[int(b1):int(b2)])
            break
        elif file_line.isdigit():
            print(b[0:int(file_line)])
            break
        else:
            print('输入错误，请重新输入')
    a.close()

print_file()
