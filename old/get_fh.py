import urllib.request
import re
from urllib import parse

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    return html

def get_magnet(html):
    p = r'<a href="(magnet:\?xt=urn:btih:[^"]+)'
    result = re.findall(p,html)
    for each in result:
        print(each)

if __name__ == '__main__':
    fh = input('Please enter the FH:')
    url = 'https://www.torrentkitty.tv/search/' + parse.quote(fh)+'/'
    get_magnet(open_url(url))
