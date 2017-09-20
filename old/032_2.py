def int_input():
    try:
        a = int(input('请输入一个整数：'))
    except ValueError :
        print('出错，您输入的不是整数。')
        int_input()
    return a

number = int_input()
