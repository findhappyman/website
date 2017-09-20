class C:
    def __init__(self, *b):
        if not b:
            print("并没有传入参数")
        else:
            print("传入了 %d 个参数，分别是：" % len(b), end='')
            for each in b:
                print(each, end=' ')
