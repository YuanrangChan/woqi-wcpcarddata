#coding:utf-8
import os,sys
from time import *
import random
 
 
EIDStart='131802FFFFF120000000'
number = random.randint(0,10000)
EIDEnd=EIDStart[:-7]+str(number-1).zfill(7)

print "EIDEnd：%s" % EIDEnd

 
print "当前工作目录为：%s" % os.getcwd()

 

if os.getcwd() != 'C:/Users/Administrator/Desktop/wcptest/rand':
    os.chdir('C:/Users/Administrator/Desktop/')
    if os.path.exists('C:/Users/Administrator/Desktop/wcptest/rand') == True:
        os.chdir('C:/Users/Administrator/Desktop/wcptest/rand')
    else:
        os.makedirs('C:/Users/Administrator/Desktop/wcptest/rand')
        os.chdir('C:/Users/Administrator/Desktop/wcptest/rand')
else:
    pass
 

provid = (001, 471, 100, 220, 531, 311, 351, 551, 210, 250, 571, 591, 898, 200, 771, 971, 270, 731, 791,
          371, 891, 280, 230, 290, 851, 871, 931, 951, 991, 431, 240, 451)

bipcode ='BIP2B950'

FourteenTime = strftime('%Y%m%d%H%M%S', localtime(time()))


rand_appcode =random.choice([str(i).zfill(3) for i in provid]) \
              + '1' +bipcode+ FourteenTime + \
              str(random.randint(000000, 999999))
			  

print u"随机生成制卡订单号appcode: %s" % rand_appcode
print len(rand_appcode)
 
filename0 = 'KeyData_'+rand_appcode+'_2_'+rand_appcode[0:3]+rand_appcode[12:26]+'.IDX'
		   
filename = 'USimMS_UpdateKey_'+rand_appcode+'_2_'+rand_appcode[0:3]+rand_appcode[12:26]+'.dat'
		   
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
 
fp.write(rand_appcode+'|2|'+rand_appcode[0:3]+'|David|13612345678|'+\
	rand_appcode[12:26]+'|MakeCardData|'+EIDStart+'|'+EIDEnd+'\n')
	
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

print "生成的制卡写卡平台模拟文件和卡数据文件见：\n C:/Users/Administrator/Desktop/wcptest: \n %s \n %s，请查收！" % (filename0,filename)
 			