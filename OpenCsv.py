import os.path
from pandas import DataFrame

csvfile = 'ECmap.csv'#词典名称
file = open(csvfile,'a+')  # 打开文件
file.seek(0)
#判断csv文件是否已经存在
size = os.path.getsize(csvfile)
if size == 0:
    #创建csv表
    data = [['','']]

    df = DataFrame(columns = ['English','中文'])
    df.to_csv(csvfile,encoding='utf-8')
    print("目标词典不存在，现已新建空白词典：" + csvfile)

else:
    print("词典打开成功！")


