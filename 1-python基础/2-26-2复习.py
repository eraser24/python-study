with open('123',mode='r',encoding='utf-8') as f,open('123.bak',mode='w',encoding='utf-8') as f2:
    for line in f:
        if 'qweasd' in line:
            line = line.replace('qweasd','ninin')
        #写文件
        f2.write(line)
#删除文件和重命名文件
import os
os.remove('123')
os.rename('123.bak','123')