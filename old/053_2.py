import urllib.request as u
d = 1
a = open('urls.txt')
b = 1
while b != '':
    b= a.readline()[:-1]
    output = str(u.urlopen(b).read())
    filename = 'url_' +str(d)
    c= open(filename,'w')
    c.write(output)
    d+= 1
    c.close()
