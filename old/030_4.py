import os
import os.path

key_word = str(input('请输入关键字：'))
answer = str(input('请问是否需要打印关键字【%s】在文件中的具体位置（YES/NO）：' % key_word))

print('================================================================')
a = list(os.walk(os.getcwd()))
result = []
lines = 0
start = 0
end = len(key_word)-1
positions = []
c = '1' 
for i in a:
    for i1 in i[2]:
        f = os.path.splitext(i1)
        if f[1] == '.txt':
            b = open(i1)
            if key_word in b.read():
                print('在文件【%s】中找到关键字【%s】' % (i[0]+'\\'+ str(i1),key_word))
                b.seek(0,0)
                while c != '':
                    c = b.readline()
                    lines += 1
                    if key_word in c:
                        print('关键字出现在第%s行' % lines,end='')
                        if answer in ['YES','Yes','yes']:
                            while end != len(c):
                                if c.find(key_word,start) != -1:
                                    positions.append(start + 1)
                                    start +=1
                                    end += 1
                            print('，第[')
                            for i2 in positions:
                                print('%s,'%i2)
                            print(']个位置')
                        print()
                print('================================================================')           

