import socket
import re
import multiprocessing


def service_client(new_socket):
    """为这个客户端返回数据"""
    # 1.接收服务器发送过来的请求，即http请求
    # GET / HTTP/1.1

    request = new_socket.recv(1024).decode("utf-8")
    request_lines = request.splitlines()
    print("")
    print(">" * 20)
    print(request_lines)

    file_name = ""
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    if ret:
        file_name = ret.group(1)
        if file_name == "/":
            file_name = "/index.html"

    try:
        f = open("./html" + file_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "-------file not found--------"
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()
        response = "HTTP/1.1 200 OK\r\n"

    new_socket.close()


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    tcp_server_socket.bind(("", 7989))
    tcp_server_socket.listen(128)

    while True:
        new_socket, client_addr = tcp_server_socket.accept()
        p = multiprocessing.Process(target=service_client, args=(new_socket))
        p.start()
        new_socket.close()

    tcp_server_socket.close()

if __name__ == '__main__':
    main()
