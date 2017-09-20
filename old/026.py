def start():
    dict1 = {}
    j=1
    k=1
    while j:
        j=1
        print('|--- 新建用户：N/n ---|')
        print('|--- 登录帐号：E/e ---|')
        print('|--- 退出程序：Q/q ---|')
        code = str(input('请输入指令代码：'))
        if code == 'N' or code == 'n':
            while 1:
                username = str(input('请输入用户名：'))
                if username in dict1:
                    print('此用户名已经被使用，请重新输入：')
                else:
                    key = str(input('请输入密码：'))
                    dict1.setdefault(username,key)
                    print('注册成功，赶紧试试登录吧^_^')
                    break
            print()
        elif code == 'E' or code == 'e':
            k=1
            while k:
                username = str(input('请输入用户名：'))
                if username not in dict1:
                    print('您输入的用户名不存在，请重新输入。')
                    k=0
                else:
                    while 1:
                        key = str(input('请输入密码：'))
                        if dict1[username] == key :
                            print('欢迎进入Henry系统！')
                            k=0
                            j=0
                            break
                        else:
                            print('您输入的用户名与密码不匹配，请重新输入。')
                            continue
            print()
            
        elif code == 'Q' or code == 'q':
            print('感谢您访向Henry系统，下次再见。')
            j=0
        else:
            print('您输入的内容有误，请重新输入。')

start()
