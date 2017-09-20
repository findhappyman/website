class Test:
    def __getattr__(self, item):
        print('该属性不存在')
