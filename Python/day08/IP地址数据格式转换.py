import socket
from binascii import hexlify


def convert_ip4_address():
    for ip_addr in ['127.0.0.1', '192.168.0.100']:
        packed_ip_addr = socket.inet_aton(ip_addr)  # aton是转换IPV4成为32位打包的二进制格式
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)  # ntoa 转换32位打包的IPV4为标准的点分十进制
        print("IP address :{} => packed: {}".format(ip_addr, hexlify(packed_ip_addr)))


if __name__ == "__main__":
    convert_ip4_address()
