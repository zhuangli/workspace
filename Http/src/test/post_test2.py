import urllib
import http.client
from time import ctime
test_data = {'ShippingMethod':' tablerate'}
test_data_urlencode = urllib.parse.urlencode(test_data)
requrl = "http://23.91.96.217:8090/cart/item/getInfo"
#headerdata = {"Host":"pay.azoyagroup.com"}
conn = http.client.HTTPConnection("23.91.96.217:8090")
conn.request(method="POST",url=requrl,body=test_data_urlencode) 
response = conn.getresponse()
res= response.read().decode()
print(res)