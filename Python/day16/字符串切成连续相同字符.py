import re

def main():
    regx="abbccddd"

    ret= re.match(r"/(\w)\1*/g",regx)
    print(ret)

if __name__ == '__main__':
    main()