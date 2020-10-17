import socket


def main():
    # 创建udp套接字
    udp_soket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_soket.sendto(b"hhahah",("10.110.46.85",8080))
    udp_soket.close()


if __name__ == '__main__':
    main()
