#coding:utf-8
import os,sys
from time import *
 

Appcode,number,MsisdnSection,IMSIStart,ICCIDStart =\
	raw_input(u"请依次输入制卡订单号,数量,号段,起始IMSI,起始ICCID,以空格分开\ "
              u"\n(模板:5911BIP2B95020180202145530123457 100 1722000 460072200000959 898602F2131820000959):\n").split()

print u"制卡订单号appcode为: %s" % Appcode
print "当前工作目录为：%s" % os.getcwd()

 

if os.getcwd() != 'C:/Users/Administrator/Desktop/woqitest':
        if os.path.exists('C:/Users/Administrator/Desktop/woqitest') == True:
            os.chdir('C:/Users/Administrator/Desktop/woqitest')
        else:
            os.makedirs('C:/Users/Administrator/Desktop/woqitest')
            os.chdir('C:/Users/Administrator/Desktop/woqitest')
else:
    pass
 
filename0 = 'KeyData_'+Appcode+'_2_'+Appcode[0:3]+'_1_'+\
           Appcode[12:26]+'.IDX'
		   
filename = 'MW_USimMS_'+Appcode+'_2_'+Appcode[0:3]+'_1_'+\
           Appcode[12:26]+'.dat'
		   
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
	Appcode[12:20]+'|MakeCardData|'+MsisdnSection+'|'+number+'|2~'+str(int(number)+1)+'\n')
fp.close()
fp=open(filename,'r')
print u"生成的制卡模拟文件头为：\n %s" % fp.read()
fp.close()

#sleep(5)
print u"开始写入卡数据文件体..."
fp=open(filename,'a')#打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
 
for i in range(int(number)):
	#IMSI = str(4600722000000)+str(i).zfill(2)#如果制卡数量小于等于99张就得补1位，完整是2位
	IMSI = str(int(IMSIStart)+i)
	ICCID = ICCIDStart[:-5]+str(int(ICCIDStart[-5:])+i).zfill(5)
	fp.write(IMSI+'|'+ICCID+'|0C3B713EAF0CD3BC63BA5ABC6C9475EF|679A21DDBB73C82E593B2B17B1000000|11111111|22222222|0123|4567|1A2B3C4D|'+\
                 IMSI[-1]+'|13800100569\n')
				 
fp.close()
  
if number <=20:
	fp=open(filename,'r')
	#fp.read()
	print u"生成的制卡模拟文件体为：\n %s" % fp.read()
	fp.close()
else:
	print u"文件总共%d行，行数太多，暂不打印！！！" % (int(number)+1)
	

print "生成的制卡握奇模拟文件和卡数据文件见：\n C:/Users/Administrator/Desktop/woqitest: \n %s \n %s，请查收！" % (filename0,filename)

a = int(raw_input("请输入数字：\n"))
print "等待%s秒后删除!" %  a
sleep(a)
print "当前工作目录为：%s" % os.getcwd()


if os.getcwd() != 'C:/Users/Administrator/Desktop':
    os.chdir('C:/Users/Administrator/Desktop')
    if os.path.exists('C:/Users/Administrator/Desktop/woqitest') == True:
        os.remove('C:/Users/Administrator/Desktop/woqitest/'+filename0)
        os.remove('C:/Users/Administrator/Desktop/woqitest/'+filename)
        os.removedirs('woqitest')
        if os.path.exists('C:/Users/Administrator/Desktop/woqitest') == False:
            print "删除目录woqitest及其文件成功！"
 
