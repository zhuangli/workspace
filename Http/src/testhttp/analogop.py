import urllib.parse
import urllib.request
import http.cookiejar
  
# cookie set
# 用来保持会话
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
    if (postdata=={}):        
        urlrequest = urllib.request.Request(hosturl)
    else:
        enpostdata = urllib.parse.urlencode(postdata).encode()
        # request url
        urlrequest = urllib.request.Request(hosturl, enpostdata, headers)
    # open url
    urlresponse = urllib.request.urlopen(urlrequest)
    # return url
    return urlresponse