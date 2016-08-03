import urllib
import urllib.request
from time import ctime
test_data = {'login[username]':' 1056204135@qq.com',
             'login[password]':'123456'}
test_data_urlencode =urllib.parse.urlencode(test_data)
requrl = "http://23.91.97.48:8023/customer/account/login/"
req = urllib.request.Request(url = requrl)
res_data = urllib.request.urlopen(req)
cookies=urllib.request.HTTPCookieProcessor()
opener=urllib.request.build_opener(cookies)
res = res_data.read()
print(res)

