#coding=utf-8
from analogop import geturlopen
from bs4 import BeautifulSoup
import time

#login=geturlopen('http://home.51cto.com/index')
#loginSoup = BeautifulSoup(login,"html.parser")
#csrf = loginSoup.find_all("head")[0].find_all("meta")[2]['content']
#print(csrf)
postd = {
    'login[username]': '1056204135@qq.com',
    'login[password]': '123456',
}
HEADER = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
    'Referer' : 'http://cn.pharmacyonline.com.au/customer/account/login',
    'Host': 'cn.pharmacyonline.com.au'
}
print('请求前的时间',time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
native=geturlopen('http://23.91.97.48:8023/customer/account/loginPost/',{}) 
print(native.read())
print('请求后的时间',time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
urlread = geturlopen('http://23.91.97.48:8023/customer/account/loginPost/', postd,HEADER)
print(urlread.read())
data_cart={
           'ShippingMethod':'tablerate'
           }
resp_cart=geturlopen('http://23.91.97.48:8023/cart/item/getInfo', data_cart)
print(resp_cart.read().decode())
#urlread = geturlopen('http://home.51cto.com/space?uid=11872330', {})
#print(urlread.read().decode())