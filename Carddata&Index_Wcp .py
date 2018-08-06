#coding:utf-8
import os,sys
from time import *
import random
 
 

Appcode,EIDStart,number =raw_input(u"请依次输入制卡订单号,EIDStart,制卡数量,以空格分开\n\
(模板:5911BIP2B95020180202145530123457 131802FFFFF120000000 1000):\n").split()

EIDEnd=EIDStart[:-7]+str(int(number)-1).zfill(7)

print "EIDEnd：%s" % EIDEnd
#print u"制卡订单号appcode为: %s" % Appcode
print "当前工作目录为：%s" % os.getcwd()
 

if os.getcwd() != 'C:/Users/Administrator/Desktop/wcptest':
        if os.path.exists('C:/Users/Administrator/Desktop/wcptest') == True:
            os.chdir('C:/Users/Administrator/Desktop/wcptest')
        else:
            os.makedirs('C:/Users/Administrator/Desktop/wcptest')
            os.chdir('C:/Users/Administrator/Desktop/wcptest')
else:
    pass
 
 
filename0 = 'KeyData_'+Appcode+'_2_'+Appcode[0:3]+'_'+Appcode[12:26]+'.IDX'
		   
filename = 'USimMS_UpdateKey_'+Appcode+'_2_'+Appcode[0:3]+'_'+Appcode[12:26]+'.dat'
		   
print filename0
print filename

fp=open(filename0,'w')
print u"开始写入秘钥索引文件内容..."
fp.write('001|002\n')
fp.close()
fp=open(filename0,'r')
print u"生成的秘钥索引文件内容为：\n %s" % fp.read()
fp.close()

#sleep(5)
fp=open(filename,'w')#打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
print u"开始写入卡数据文件头..."
 
fp.write(Appcode+'|2|'+Appcode[0:3]+'|David|13612345678|'+\
	Appcode[12:26]+'|MakeCardData|'+EIDStart+'|'+EIDEnd+'\n')
fp.close()
fp=open(filename,'r')
print u"生成的制卡模拟文件头为：\n %s" % fp.read()
fp.close()

#sleep(5)
print u"开始写入卡数据文件体..."
fp=open(filename,'a')#打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。

 
 
for i in range(int(number)):
	fp.write(EIDStart[:-7]+str(i).zfill(7)+'|'+'3467012345abcde0456783232809'+str(i).zfill(4)+'|3467012345abcde0456873232809'+str(i).zfill(4)+'|3467012345abcde0457683232809'+str(i).zfill(4)+'\n')
				 
fp.close()
 
if int(number) <=20:
	fp=open(filename,'r')
	#fp.read()
	print u"生成的制卡模拟文件体为：\n %s" % fp.read()
	fp.close()
else:
	print u"文件总共%d行，行数太多，暂不打印！！！" % (int(number)+1)
	

print u"生成的制卡握奇模拟文件和卡数据文件见：\n C:/Users/Administrator/Desktop/wcptest: \n %s \n %s，请查收！" % (filename0,filename)

a = int(raw_input(u"请输入数字：\n"))
print u"等待%s秒后删除？" %  a
sleep(a)
print u"当前工作目录为：%s" % os.getcwd()


if os.getcwd() != 'C:/Users/Administrator/Desktop':
    os.chdir('C:/Users/Administrator/Desktop')
    if os.path.exists('C:/Users/Administrator/Desktop/wcptest') == True:
        os.remove('C:/Users/Administrator/Desktop/wcptest/'+filename0)
        os.remove('C:/Users/Administrator/Desktop/wcptest/'+filename)
        os.removedirs('wcptest')
        if os.path.exists('C:/Users/Administrator/Desktop/wcptest') == False:
            print "删除目录woqitest及其文件成功！"
