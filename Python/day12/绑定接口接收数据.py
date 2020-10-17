import socket


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定本地信息
    localaddr = ("", 7789)
    udp_socket.bind(localaddr)  #必须绑定自己的ip 和 port 其他的不行
    # 接收数据
    recv_data = udp_socket.recvfrom(1024)
    #  recv_data这个变量中存储的是一个元组(接收到的数据,(发送方的端口))
    recv_msg = recv_data[0]  # 存储接收到的数据
    send_addr = recv_data[1]  # 存储发送方的地址信息
    # 打印接收到的数据
    # print(recv_data)
    print("%s:%s" % (str(send_addr), recv_msg.decode("gbk")))
    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()
