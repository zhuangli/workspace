#coding=utf-8
import urllib.request ,json
request = urllib.request.Request('http://23.91.96.217:8090/o_customer/info/getCustomer?_=1468403159578')
#request.add_header('User-Agent', 'fake-client')
response = urllib.request.urlopen(request)
resultDict2=response.read().decode();
print(resultDict2)
resultDict = json.loads(str(resultDict2))#读取json变为dict
print(resultDict['loginUrl'])
#logging.info('--re:%s-,status:%s,msg:%s-----' %(resultDict,resultDict['Status'],resultDict['Message']))
#status = resultDict['loginUrl']
#dataDict=status['url_path']
#print(status['meta_info'])
#print(status)