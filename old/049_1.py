def myPrime():
    number =0
    while True:
        if is_Prime(number):
            yield number
        number += 1
def is_Prime(n):
    m = n//2
    t=0
    for i in range(2,m):
        if n % i == 0 :
            return False
    return True

sum = 0
for i in myPrime():
    if i <= 2000000:
        sum += i
    else:
        print(sum)
        break
