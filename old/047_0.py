class CountList:
    def __init__(self, *args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)), 0)
        self.inter = 0
    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        self.count[key] += 1
        return self.values[key]
    def __setitem__(self, key, value):
        self.values[key]= value
    def __delitem__(self, key):
        del self.values[key]
        for each in range(key,len(self.values)):
            self.count[each]=self.count[each+1]
    def counter(self,value):
        return self.count[self.values.index(value)]
    def append(self,value):
        self.values.append(value)
        self.count.update({value:0})
    def pop(self,index=-1):
        self.values.pop(index)
        for each in range(index,len(self.values)):
            self.count[each]=self.count[each+1]
    def remove(self,value):
        self.values.remove(value)
        for each in range(self.values.index(value),len(self.values)):
            self.count[each]=self.count[each+1]
    def insert(self,position,value):
        self.values.insert(position,value)
        self.count.update({len(self.values)-1:0})
        for each in range(position,len(self.values)-1):
            self.count[each]=self.count[each-1]
    def clear(self):
        self.values.clear()
        self.count.clear()
    def reverse(self):
        self.values.reverse()
        for each in range(len(self.values)//2):
            self.inter = self.count[each]
            self.count[each] = self.count[len(self.values) - each - 1]
            self.count[len(self.values) - each - 1] = self.inter
