import pandas as pd
import csv

csvfile = 'ECmap.csv'
csvPD = pd.read_csv(csvfile)
while(1):
    print("请输入要删除的英文单词：（只支持精确查找，输入0退出）")
    en_Name = input()
    flag = 0
    if en_Name == '0':
        break

    else:
        for i in range(len(csvPD)):
            if str(csvPD['English'][i])==en_Name:
                flag = 1
                new=csvPD.drop([i])#删除第i行数据
                new.to_csv(csvfile,index=0)
                # new=csvPD.drop(["Unnamed: 0"],axis=1)
                # new.to_csv(csvfile,index=0)
                print("删除" + en_Name + "成功！")
                break;
        if flag == 0:
            print("字典库中未找到这个单词！")