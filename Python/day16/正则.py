import re

def main():
    email=input("请输入一个邮箱地址：")
    ret= re.match(r"[a-zA-Z_0-9]{4,20}@163\.com$",email)
    if ret:
        print("符合要求")
    else:
        print("不符合要求")

if __name__ == '__main__':
    main()