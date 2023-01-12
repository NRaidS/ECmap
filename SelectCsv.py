import pandas as pd

csvfile = 'ECmap.csv'#词典名称
csvPD=pd.read_csv(csvfile)
# print(csvPD)
while(1):
    print("请输入要查找的英文单词：（只支持精确查找，输入1查找全部，输入0退出）")
    en_Name = input()
    flag = 0
    if en_Name == '0':
        break

    elif en_Name == '1':
        for i in range(len(csvPD)):
            if str(csvPD['English'][i])!='':
                flag = 1
                print(csvPD['English'][i] + ' ' + csvPD['中文'][i])
        if flag == 0:
            print("字典库中没有单词！")
            break
    else:
        for i in range(len(csvPD)):
            if str(csvPD['English'][i])==en_Name:
                print("该单词已添加到字典库！")
                flag = 1
                print(csvPD['English'][i] + ' ' + csvPD['中文'][i])
                break;
        if flag == 0:
            print("字典库中未找到这个单词！")