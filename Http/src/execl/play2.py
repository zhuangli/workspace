from testframe import *  
from xxx_server_case import *  
import xxx_server_case  
  
#��Ʒϵͳ�ӿڲ���  
#���ò��Ի���  
xxx_server_case.excelobj=create_excel(os.getcwd()+'/TestDir/xxx_Testcase.xls')  
xxx_server_case.com_ipport=xxx.com'  
  
#Add testsuite begin  
run("xxx_book_list", 4)  
#Add other suite from here  
#Add testsuite end  
  
statisticresult(xxx_server_case.excelobj)  
xxx_server_case.excelobj.close()  