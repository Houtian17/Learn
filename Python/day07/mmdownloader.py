from time import time
from threading import Thread

import requests


class DownloadHanlder(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def getHTMLText(self):
        maxTryNum = 20
        for tries in range(maxTryNum):
            try:
                kv = {"user-agent": "Mizilla/5.0"}
                response = requests.get(self, headers=kv, timeout=10)
                return response.text
            except:
                if tries < (maxTryNum - 1):
                    continue
                else:
                    print("Has tried %d times to access url %s, all failed!" % (maxTryNum, url))
                    break

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('/Users/kristennn/Documents/notes' + filename, 'wb') as f:
            f.write(resp.content)





def main():
    # 通过requests模块的get函数获取网络资源
    resp = requests.get(
        'http://api.tianapi.com/meinv/?key=772a81a51ae5c780251b1f98ea431b84&num=10')
    # 将服务器返回的JSON格式的数据解析为字典
    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        # 通过多线程的方式实现图片下载
        DownloadHanlder(url).start()



if __name__ == '__main__':
    main()