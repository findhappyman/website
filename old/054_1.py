import re
import urllib.request
from http.cookiejar import CookieJar

# ����ĵ�¼url
loginurl = 'https://www.douban.com/accounts/login'
cookie = CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor)

data = {
    "form_email": "your email",
    "form_password": "your password",
    "source": "index_nav"
}
data = {}
data['form_email'] = '����˺�'
data['form_password'] = '�������'
data['source'] = 'index_nav'

response = opener.open(loginurl, urllib.parse.urlencode(data).encode('utf-8'))

# ��֤�ɹ���ת����¼ҳ
if response.geturl() == "https://www.douban.com/accounts/login":
    html = response.read().decode()

    # ��֤��ͼƬ��ַ
    imgurl = re.search('<img id="captcha_image" src="(.+?)" alt="captcha" class="captcha_image"/>', html)
    if imgurl:
        url = imgurl.group(1)
        # ����֤��ͼƬ������ͬĿ¼��
        res = urllib.request.urlretrieve(url, 'v.jpg')

        # ��ȡcaptcha-id����
        captcha = re.search('<input type="hidden" name="captcha-id" value="(.+?)"/>', html)

        if captcha:
            vcode = input('������ͼƬ�ϵ���֤�룺')
            data["captcha-solution"] = vcode
            data["captcha-id"] = captcha.group(1)
            data["user_login"] = "��¼"

            # �ύ��֤����֤
            response = opener.open(loginurl, urllib.parse.urlencode(data).encode('utf-8'))

            # ��¼�ɹ���ת����ҳ '''
            if response.geturl() == "http://www.douban.com/":
                print('��¼�ɹ���')
