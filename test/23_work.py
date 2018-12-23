import  zipfile
import os
import sys
import time

#可以前面加 r 来是\\ 变成 \
source1 = r"F:\python\code\Test\source"
source2 = "F:\\python\\code\\Test\\source2"

#让用户输入comment来区别压缩文件
comment = input("please input zip comment:")
if(len(comment) == 0):
	comment = ""

target_dir = "F:\\python\\code\\Test\\target"
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') +"_"+\
comment.replace(" ","_")+ '.zip'
print("zip fileName:"+target)

if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    print("mkdir {} success!".format(target_dir))
else:
    print("target dir is exist, not should create.")

#使用 zipfile来压缩文件
zipfiles = zipfile.ZipFile(target,'w')
if os.path.isdir(source1):
	print("source1 is a dir")
	for child in os.listdir(source1):
		zipfiles.write(child)
		print("write "+child+" to "+target_dir+" success!")
	zipfiles.close()
else:
	print("sorce1 is not a dir.")
