def myRev(list):
    index = len(list)-1
    while index >= 0:
        yield list[index]
        index -=1
for i in myRev("FishC"):
    print(i, end='')
