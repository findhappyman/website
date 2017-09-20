import chardet as ch
import urllib.request as u

url = input('请输入URL：')
feedback = ch.detect((u.urlopen(url).read()))
print('该网页使用的编码是：%s'% feedback['encoding'])
