import socket

def get_remote_machine_info():
    remote_host='www.sina.com'
    try:
        print("ip address:",socket.gethostbyname(remote_host))
    except socket.error as err_msg:
        print(remote_host,err_msg)


if __name__ == '__main__':
    get_remote_machine_info()