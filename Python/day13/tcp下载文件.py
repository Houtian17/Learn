import socket


def main():
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 获取服务器ip port
    dest_ip = input("请输入下载服务器的ip：")
    dest_port = int(input("请输入下载服务器的端口："))
    # 链接服务器
    tcp_socket.connect((dest_ip, dest_port))
    # 获取下载的文件名字
    download_file_name = input("请输入要下载的文件名：")
    # 将文件的名字发送到服务器
    tcp_socket.send(download_file_name.encode("utf-8"))
    # 接收文件中的数据
    recv_data = tcp_socket.recv(1024 * 1024)
    # 保存接收到的数据保存到文件
    with open("[新]" + download_file_name, "wb")as f:
        f.write(recv_data)

    # 关闭套接字


if __name__ == '__main__':
    pass
