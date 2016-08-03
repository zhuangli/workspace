#coding=utf-8
from analogop import geturlopen
from bs4 import BeautifulSoup

login=geturlopen('http://home.51cto.com/index')
loginSoup = BeautifulSoup(login,"html.parser")
csrf = loginSoup.find_all("head")[0].find_all("meta")[2]['content']
print(csrf)
postd = {
     '_csrf':csrf,
    'LoginForm[username]': '13620900559',
    'LoginForm[password]': 'woshidiyi123',
    'LoginForm[rememberMe]':'0',
    'login-button':'登 录'
}
HEADER = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
    'Referer' : 'http://home.51cto.com/index',
    'Host': 'home.51cto.com'
}
  
  
urlread = geturlopen('http://home.51cto.com/index', postd,HEADER)
print(urlread.read().decode())
urlread = geturlopen('http://home.51cto.com/space?uid=11872330', {})
print(urlread.read().decode())