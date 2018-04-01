# coding:utf-8  fxb_qzyx@163.com
"""
1.tcp的socket通信；
2.使用shutdown来关闭socket的功能:实现单项通信
    SHUT_RDWR(2)：关闭读写，即不能使用send/write/recv/read
    SHUT_RD(1)：关闭读，即不能使用read/recv
    SHUT_WR(0):关闭写功能，即不能使用send/write
    除此之外，还将缓冲区中的内容清空
"""

import socket
import traceback


def send_commend_tcp_socket(host_ip, port, commend_str):
    """
    :brief :tcp的socket客户端
    :param host_ip: 服务器端ip
    :param port: 服务器端端口
    :param commend_str: 发送给服务器端的消息
    :return: 返回服务器发送过来的消息
    """
    result = "Fail"
    try:
        # 创建socket对象
        socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 建立socket连接
        socket_obj.connect((str(host_ip), int(port)))
        # 将发送的消息转换为byte类型
        commend_bytes = bytes(commend_str, encoding='utf-8')
        # # 发送消息
        socket_obj.sendall(commend_bytes)
        # 接收服务器端发过来的消息
        result = socket_obj.recv(1024 * 10)
        # 关闭读：不能接收服务器端发送过来的消息，告诉服务器消息已接收完毕！这个在用java的serversocket通信时用到过
        # socket_obj.shutdown(1)
    except Exception as e:
        # 打印红色字体:\033[显示方式;前景色；背景色 '具体内容' \033[0m
        # print("\033[0;31;0m{}\033[0m".format(e))
        traceback.print_exc()  # 这里不能将变量e传进去
    finally:
        # 关闭socket
        socket_obj.close()

    print('hello world')

    return result


if __name__ == "__main__":
    send_commend_tcp_socket('localhost', 50000, 'hello')
    pass

