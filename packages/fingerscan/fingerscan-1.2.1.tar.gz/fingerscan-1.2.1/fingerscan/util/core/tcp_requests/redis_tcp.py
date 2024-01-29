"""
@Project ：指纹识别 
@File    ：redis_tcp.py
@IDE     ：PyCharm 
@Author  ：zhizhuo
@Date    ：2023/10/20 09:47 
"""
import json
from util.socket import SocketSend
from util.core.cert import GetSSLInfo


class ClientRedisTcpClass:
    """
    redis 链接tcp类，用来验证是否是未授权的
    """

    def __init__(self):
        """
        初始化操作
        """
        self.send_data = "*1\r\n$4\r\ninfo\r\n"

    def _send_data(self, url):
        """
        调用tcp发送tcp数据
        :param url:url地址
        :return:json
        """
        host_list = GetSSLInfo(url=url).get_domain_info()
        host = host_list.get("host")
        port = host_list.get("port")
        res = SocketSend.send_tcp(host=host, port=port, is_ssl=False,
                                  send_data=self.send_data)
        return res

    def send_redis_tcp(self, url):
        """
        发送redis链接tcp操作
        :param url:url地址
        :return:json
        """
        return json.dumps(self._send_data(url))


redis_client = ClientRedisTcpClass()
