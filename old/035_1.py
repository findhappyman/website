import easygui as g

list_account = []
while 1:
    list_account = g.multenterbox(msg= '【*真实姓名】为必填项。\n【*手机号码】为必填项。\n【*E-mail】为必填项。',title = '账号中心',fields=('*用户名','*真实姓名','固定电话','*手机号码','QQ','*E-mail'))
    if ' ' in list_account[0,1,3,5]:
        pass
    else:
        break
print(list_account)
