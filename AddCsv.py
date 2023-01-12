import csv
import pandas as pd

csvfile = 'ECmap.csv'#词典名称


#判断是否是纯英文
def is_all_eng(strs):
    import string
    for i in strs:
        if i not in string.ascii_lowercase+string.ascii_uppercase:
            return False
    return True

#判断是否是纯中文
def is_all_chinese(strs):
    for i in strs:
        if not '\u4e00' <= i <= '\u9fa5':
            return False

flag = 0
while flag == 0:

    #输入英文
    while(1):
        print("请输入单词英文：（按0退出添加程序）（不支持任何符号）")
        en_Name = input()
        if en_Name == "0":
            flag = 1
            break;
        elif is_all_eng(en_Name) == False:
            print("请输入正确的英文单词格式！")
        elif en_Name == '':
            print("请输入正确的英文格式！")
        else:

            flag = 0;
            csvPD=pd.read_csv(csvfile)
            for i in range(len(csvPD)):
                if str(csvPD['English'][i])==en_Name:
                    flag = 1;
                    print(en_Name + "已存在！")
                    break
            if flag == 0:
                print("已输入单词英文：" + en_Name)
                break

    if flag == 1:
        print("已退出添加程序！")
        break
    #输入中文（中文符号都不可？）
    while(1):
        print("请输入单词中文：（按0退出添加程序）（不支持任何符号）")
        cn_Name = input()
        if cn_Name == '0':
            flag = 1
            break
        elif is_all_chinese(cn_Name) == False:
            print("请输入正确的中文格式！")
        elif cn_Name == '':
            print("请输入正确的中文格式！")
        else:
            print("已输入单词中文：" + cn_Name)
            break

    if flag == 0:
        lst = ['',en_Name, cn_Name]
        with open(csvfile, 'a+', newline='',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(lst)
        print("已添加单词组：" + en_Name + " " + cn_Name)
    else:
        print("已退出添加程序！")
        break