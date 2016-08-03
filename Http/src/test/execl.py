# encoding=utf-8      
  
import xlrd,xlwt                 
import urllib.request ,json,logging
from pyExcelerator import * 
 
xlsfile = r'D:\Book1.xlsx'   
book = xlrd.open_workbook(xlsfile)     
  

sheet_name=book.sheet_names()[0]          
print(sheet_name)  
sheet1=book.sheet_by_name(sheet_name) 
sheet0=book.sheet_by_index(0)    
  
nrows = sheet0.nrows      
ncols = sheet0.ncols   
  

  
row_data = sheet0.row_values(0)  
col_data = sheet0.col_values(0)  
  

cell_value1 = sheet0.cell_value(1,0)  
print(cell_value1)  
cell_value2 = sheet0.cell(1,1)
print(cell_value2)

request = urllib.request.Request(cell_value1)
#request.add_header('User-Agent', 'fake-client')
response = urllib.request.urlopen(request)
print(response)
resultDict = json.loads(response.read().decode())
#logging.info('--re:%s-,status:%s,msg:%s-----' %(resultDict,resultDict['Status'],resultDict['Message']))
status = resultDict['Data']
#dataDict=status['url_path']
print(status['meta_info'])
print(status)



bk = xlrd.open_workbook(xlsfile)
shxrange = range(bk.nsheets)

    sh = bk.sheet_by_name("Sheet1")

nrows = sh.nrows
ncols = sh.ncols
print "nrows %d, ncols %d" % (nrows,ncols)

cell_value = sh.cell_value(1,1)
#print cell_value

row_list = []
mydata = []
for i in range(1,nrows):
    row_data = sh.row_values(i)
    pkgdatas = row_data[3].split(',')
    #pkgdatas.split(',')
    #获取每个包的前两个字段
    for pkgdata in pkgdatas:
        pkgdata = '.'.join((pkgdata.split('.'))[:2])
        mydata.append(pkgdata)
    #将列表排序
    mydata = list(set(mydata))
    print mydata
    #将列表转化为字符串
    mydata = ','.join(mydata)
    #写入数据到每行的第一列
    ws.write(i,0,mydata)
    mydata = []
    row_list.append(row_data[3])
#print row_list
w.save('mini.xls')
