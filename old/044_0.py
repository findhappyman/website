import time as t
class Mytimer:
    def __init__(self):
        self.unit =['年','月','日','时','分','秒']
        self.assist = [0,12,30,24,60,60]
        self.lasted = []
        self.begin = 0
        self.end = 0
        self.prompt = '未开始记时'
    def __add__(self, other):
        prompt = '总共运行'
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index])+ self.unit[index])
        return self.prompt
    def __str__(self):
        return self.prompt
    def __repr__(self):
        return self.prompt
    # 开始计时
    def start(self):
        self.begin = t.localtime()
        print('开始计时...')
    # 结束计时
    def stop(self):
        if self.begin:
            self.prompt = '共持续'
            self.end = t.localtime()
            self._last()
            print('停止计时！')
        else:
            print('还未开始计时')

    # 计算持续时间
    def _last(self):
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]< 0:
                self.lasted[index] += self.assist[index]
                self.lasted[index-1] -= 1
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])

