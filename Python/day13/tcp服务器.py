import socket

def main():
    # 买个手机创建套接字，
    tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # 插入手机卡，绑定本地信息，bind
    tcp_server_socket.bind(("",7788))

    # 将手机设置成正常的 响铃模式 让默认的套接字由主动变为被动 listen
    tcp_server_socket.listen(128)

    print("-----------1----------")
    # 等待别人的电话到来 等待客户端的链接 accept
    new_client_socket,client_addr=tcp_server_socket.accept()
    print("-----------2----------")

    print(client_addr)

    # 接收客户端发来的请求
    recv_data=new_client_socket.recv(1024)
    print(recv_data)

    # 回送一部分数据给客户端
    new_client_socket.send("hahahahaha---ok----".encode("utf-8"))

    # 关闭套接字
    new_client_socket.close()
    tcp_server_socket.close()



if __name__ == '__main__':
    main()