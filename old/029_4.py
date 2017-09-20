def fun():
    filename = input('请输入文件名：')
    old_word = input('请输入需要替换的单词或字符')
    
new_word = input('请输入新的单词或字符')
    a = open(filename,'r+')
    old_word_lenth = len(old_word)
    new_word_lenth = len(new_word)    
    for i in a:
        if i == old_word:
            
