import socket


def main():
    upd_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    dest_ip = input("请输入对方的ip：")
    dest_port = int(input("请输入对方的端口号："))

    send_data = input("请输入要发送的数据：")

    upd_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))

    recv_data=upd_socket.recvfrom(1024)

    upd_socket.close()


if __name__ == '__main__':
    main()
