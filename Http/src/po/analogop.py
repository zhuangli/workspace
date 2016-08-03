#coding=utf-8
import urllib.parse
import urllib.request
import http.cookiejar
import socket
  
# cookie set
# �������ֻỰ
cj = http.cookiejar.LWPCookieJar()
cookie_support = urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler)
urllib.request.install_opener(opener)
  
# default header
HEADER = {
   
}
  
# operate method
def geturlopen(hosturl, postdata = {}, headers = HEADER):
    # encode postdata
    tryTimes = 0
    while True:
        if (tryTimes>20):
            print("请求失败")
            break
        try:
            if (postdata=={}):
                req = urllib.request.Request(hosturl)
            else:
                req = urllib.request.Request(hosturl,urllib.parse.urlencode(postdata).encode())
            reqest = urllib.request.urlopen(req)
            tryTimes = tryTimes +1
        except socket.error:
            print("有异常")
        else:
            break
    return reqest 
