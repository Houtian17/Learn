import re

ret = re.match(r"([a-zA-Z0-9_]{4-20})@(163|126)\.com$", "hzb@163.com")
print(ret)
