import http.client
import json,logging
conn = http.client.HTTPConnection('sandbox.haituncun.com')  
conn.request("GET", "/m_catalog/product/list?catalogId=243&sale=desc&page=1&perNum=20")  
rsps = conn.getresponse()  
data = rsps.read().decode()
print (rsps.status,  rsps.reason)
print (rsps.msg)
print (data) 
resultDict = json.loads(data)
print(resultDict['Status'])
logging.info('--re:%s-' %(resultDict))
if rsps.status==200:
    print('nnnn')
conn.close()  

