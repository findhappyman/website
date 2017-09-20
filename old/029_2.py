def print_file():
    filename = str(input('请输入要打开的文件：'))
    file_line = int(input('请输入需要显示该文件前几行：'))
    a = open(filename)
    while file_line:
        b = a.readline()
        print(b,end='')
        file_line -= 1
    a.close()

print_file()
