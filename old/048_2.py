class MyRev:
    def __init__(self,str):
        self.string = str.reversed()
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.i += 1
        return self.string[self.i]
