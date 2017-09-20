import pickle

def pickle_in(boy_file,girl_file):
    boy = []
    girl = []
    file = open('record.txt')
    while 1:   
        content = file.readline()
        if '小甲鱼:' in content:
            boy.append(content[3:])
        elif '小客服:' in content:
            girl.append(content[3:])
        else:
            file_boy = open(boy_file,'wb')
            file_girl = open(girl_file,'wb')
            pickle.dump(boy,file_boy)
            pickle.dump(girl,file_girl)
            file_boy.close()
            file_girl.close()
            break

pickle_in('boy_1.txt','girl_1.txt')
pickle_in('boy_2.txt','girl_2.txt')
pickle_in('boy_3.txt','girl_3.txt')
