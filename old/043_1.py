class Word(str):
    def __new__(cls, string):
        if isinstance(string,str):
            string = len(string)
            return str.__new__(cls,string)
        else:
            print('输入字符串有误')


