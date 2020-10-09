# 你可以通过socket实例对象的gettimeout()及settimeout()方法来获取与设置timeout的值。

import socket

def test_socket_timeout():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("default socket timeout:{}".format(s.gettimeout()))
    s.settimeout(100)
    print("current socket timeout:{}".format(s.gettimeout()))

if __name__ == '__main__':
    test_socket_timeout()