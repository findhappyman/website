import time as t
class Mytimer:
    def __init__(self,func,count=1000000):
        self.lasted = 0
        self.prompt = '未开始计时'
        self.begin = 0
        self.end = 0
        self.i = count
        self.func = func
    def __add__(self, other):
        return str(self.lasted +other.lasted) +'秒'
    def __str__(self):
        return self.prompt
    def __repr__(self):
        return self.prompt
    # 开始计时
    def start(self):
        self.variable = t.perf_counter()
        self.begin = self.variable
        print('开始计时...')
    # 结束计时
    def stop(self):
        if self.begin:
            self.variable = t.perf_counter()
            self.end = self.variable
            self.lasted = self.end - self.begin
            self.prompt = str(self.lasted) +'秒'
            print('停止计时！')
        else:
            print('还未开始计时')
        self.begin = 0
        self.end = 0
    def set_timer(self):
        self.variable = t.process_time()
        # 运行函数 1000000次，并记录用时
    def timing(self):
        self.start()
        while self.i:
            self.func()
            self.i -=1
        self.stop()