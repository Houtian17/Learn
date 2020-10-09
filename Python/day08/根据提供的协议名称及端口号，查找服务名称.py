import socket


def find_service_name():
    protocolname = 'tcp'
    for port in [80, 25, 21]:
        print("Port: {} => service name: {}".format(port, socket.getservbyport(port, protocolname)))
        print("Port: {} => service name: {}".format(53, socket.getservbyport(53, 'udp')))


if __name__ == '__main__':
    find_service_name()

