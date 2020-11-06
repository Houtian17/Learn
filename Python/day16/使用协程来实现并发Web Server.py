import socket
import re
import gevent
from gevent import monkey
monkey.patch_all()


def handle_request(new_socket):
    # 接收请求
    recv_msg = ""
    recv_msg = new_socket.recv(1024).decode("utf-8")
    if recv_msg == "":
        print("recv null")
        new_socket.close()
        return

    # 从请求中解析出URI
    recv_lines = recv_msg.splitlines()
    print(recv_lines.__len__())
    # 使用正则表达式提取出URI
    ret = re.match(r"[^/]+(/[^ ]*)", recv_lines[0])
    if ret:
        # 获取URI字符串
        file_name = ret.group(1)
        # 如果URI是/，则默认返回index.html的内容
        if file_name == "/":
            file_name = "/index.html"

    try:
        # 根据请求的URI，读取相应的文件
        fp = open("." + file_name, "rb")
    except:
        # 找不到文件，响应404
        response_msg = "HTTP/1.1 404 NOT FOUND\r\n"
        response_msg += "\r\n"
        response_msg += "<h1>----file not found----</h1>"
        new_socket.send(response_msg.encode("utf-8"))
    else:
        html_content = fp.read()
        fp.close()
        # 响应正确 200 OK
        response_msg = "HTTP/1.1 200 OK\r\n"
        response_msg += "\r\n"

        # 返回响应头
        new_socket.send(response_msg.encode("utf-8"))
        # 返回响应体
        new_socket.send(html_content)

    # 关闭该次socket连接
    new_socket.close()


def main():
    # 创建TCP SOCKET实例
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # # 设置重用地址
    # tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定地址（默认本机IP）和端口
    tcp_server_socket.bind(("", 7893))
    # 监听
    tcp_server_socket.listen(128)
    # 循环接收客户端连接
    while True:
        new_socket, client_addr = tcp_server_socket.accept()
        # 启动一个协程来处理客户端的请求
        gevent.spawn(handle_request, new_socket)

    # 关闭整个SOCKET
    tcp_server_socket.close()


if __name__ == "__main__":
    main()