print ('|----欢迎进入通讯录-----|\n|---1：查询联系人资料---|\n|---2：插入联系人资料---|\n|---3：删除已有联系人---|\n|---4：退出通讯录程序---|')
dict1 = {}
j=1

k=1
while j:
            number1 = int(input('请输入相关的指令代码：'))
            if number1 == 1:
                name = input('请输入联系人姓名：')
                if name not in dict1:
                    number2 = str(input('该联系人不在通讯录，是否需要新增（是/否)：'))
                    while k:
                        if number2 == '是':
                            phone = input('请输入用户联系电话：')
                            dict1[name] = phone
                            k = 0
                        elif number2 == '否':
                            k = 0
                        else:
                            print('输入错误，请重新输入')
                            k = 1
                else:
                    print('%s：%s'% (name, dict1[name]))
                print()
            elif number1 == 2:
                name = input('请输入联系人姓名：')
                if name in dict1:
                        print('您输入的姓名在通讯录中已存在--> %s：%s'% (name , dict1[name]))
                        number2 = input('是否修改用户资料（是/否)：')
                        while k:
                            if number2 == '是':
                                phone = input('请输入用户联系电话：')
                                dict1[name] = phone
                                k = 0
                            elif number2 == '否':
                                k = 0
                            else:
                                print('输入错误，请重新输入')
                                k = 1     
                        
                else:
                        phone = input('请输入用户联系电话：')
                        dict1[name] = phone
                print()
            elif number1 == 3:
                name = input('请输入需要删除的联系人姓名：')
                if name in dict1:
                    del dict1[name]
                    print('联系人已删除。')
                else:
                    print('此联系人不在通讯录中。')
                print()
            elif number1 == 4:
                j=0
                print('|--- 感谢使用通讯录程序 ---|')
                print('\n')
            else:
                print('输入失败，请重新输入。')
                print()
                        
