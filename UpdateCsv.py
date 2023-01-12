import pandas as pd
import csv

csvfile = 'ECmap.csv'
df = pd.read_csv(csvfile, encoding='utf-8')

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

while(1):
    print("请输入目标自然行或者目标英文单词： （输入0退出）")
    target = input()
    if target == '0':
        break
    elif is_all_eng(target) == False:#不是全英文
        if target.isdigit() == False:#不是全英文也不是全数字
            print("输入错误！请重新输入")
            continue
        else:#全数字，自然行处理
            target = int(target)
            if len(df)  + 1 < target or target <= 1:#数字范围不符合
                print("该行中不存在单词！请重新输入")
                continue
            else:
                #处理行
                target -= 2
                print("当前行的单词为：" + str(df['English'][target]) + " " + str(df['中文'][target]))

                while(1):
                    print("请输入要修改的英文：（按0跳过）")
                    new_En = input()
                    if new_En == "0":
                        break
                    elif is_all_eng(new_En) == False:
                        print("请输入正确的英文单词格式！")
                        continue

                    else:
                        fff = 0
                        for i in range(len(df)):
                            if str(df['English'][i])==new_En:
                                fff = 1
                                break;
                        if fff == 0:#词典里没有的单词才能加
                            #必须对副本进行操作，不然会出警告
                            dfc = df['English'].copy()
                            dfc.loc[target] = new_En
                            df['English'] = dfc
                            df.to_csv(csvfile,index=0)
                            print("修改英文成功！")
                            break;
                        else:
                            print("单词已存在！请重新输入")
                            continue
                while(1):
                    print("请输入要修改的中文：（按0跳过）")
                    new_Cn = input()
                    if new_Cn == "0":
                        break
                    elif is_all_chinese(new_Cn) == False:
                        print("请输入正确的中文单词格式！")
                        continue
                    else:
                        #必须对副本进行操作，不然会出警告
                        dfc = df['中文'].copy()
                        dfc.loc[target] = new_Cn
                        df['中文'] = dfc
                        df.to_csv(csvfile,index=0)
                        print("修改中文成功！")
                        break;

    else:#是纯英文
        flag = 0
        for i in range(len(df)):
            if str(df['English'][i])==target:
                print("当前行的单词为：" + str(df['English'][i]) + " " + str(df['中文'][i]))
                flag = 1
                while(1):
                    print("请输入要修改的英文：（按0跳过）")
                    new_En = input()
                    if new_En == "0":
                        break
                    elif is_all_eng(new_En) == False:
                        print("请输入正确的英文单词格式！")
                        continue
                    else:
                        fff = 0
                        for i in range(len(df)):
                            if str(df['English'][i])==new_En:
                                fff = 1
                                break;
                        if fff == 0:#词典里没有的单词才能加
                            #必须对副本进行操作，不然会出警告
                            dfc = df['English'].copy()
                            dfc.loc[i] = new_En
                            df['English'] = dfc
                            df.to_csv(csvfile,index=0)
                            print("修改英文成功！")
                            break;
                        else:
                            print("单词已存在！请重新输入")
                            continue
                while(1):
                    print("请输入要修改的中文：（按0跳过）")
                    new_Cn = input()
                    if new_Cn == "0":
                        break
                    elif is_all_chinese(new_Cn) == False:
                        print("请输入正确的中文单词格式！")
                        continue
                    else:
                        #必须对副本进行操作，不然会出警告
                        dfc = df['中文'].copy()
                        dfc.loc[i] = new_Cn
                        df['中文'] = dfc
                        df.to_csv(csvfile,index=0)

                        print("修改中文成功！")
                        break
                break
        if flag == 0:
            print("字典库中未找到这个单词！")