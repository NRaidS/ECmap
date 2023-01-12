import os

print("欢迎使用词典系统！")
os.system("OpenCsv.py")
while(1):

    print("请输入需要进行的操作的对应数字：（1查询，2添加，3删除，4修改，0退出）")

    opt = input()
    if opt == "0":
        print("感谢您的使用！")
        break;

    elif opt == "1":
        os.system("SelectCsv.py")
    elif opt == "2":
        os.system("AddCsv.py")
    elif opt == "3":
        os.system("DeleteCsv.py")
    elif opt == "4":
        os.system("UpdateCsv.py")
    else:
        print("输入有误！请重新输入！")
