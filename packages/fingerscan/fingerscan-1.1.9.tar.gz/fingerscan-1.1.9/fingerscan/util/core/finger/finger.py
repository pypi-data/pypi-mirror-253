"""
@Project ：指纹识别 
@File    ：finger.py
@IDE     ：PyCharm 
@Author  ：zhizhuo
@Date    ：2023/10/18 14:50 
"""
import json
from urllib.parse import urlparse


class GetFingerClass:
    """
    指纹匹配处理类
    """

    def __init__(self):
        """
        初始化操作
        """
        finger_path = 'config/finger.json'
        with open(finger_path, 'r', encoding='utf-8') as file:
            self.finger_list = json.load(file)

    def _run_get_finger(self, title: str, icon_hash: str, headers: str, res: str):
        """
        开始匹配指纹
        :param title:title
        :param icon_hash:icon_hash
        :param headers:headers
        :param res:response
        :return:cms数据
        """
        html = res.text
        finger_list = self.finger_list.get('fingerprint')
        for f in finger_list:
            cms = f.get('cms')
            method = f.get('method')
            location = f.get('location')
            keywords = f.get('keyword')
            if html is not None:
                if method == 'keyword' and location == 'body':
                    found_keywords = all(keyword in html for keyword in keywords)
                    if found_keywords:
                        return cms

                elif method == 'icon_hash' and location == 'body':
                    found_keywords = all(keyword in str(icon_hash) for keyword in keywords)
                    if found_keywords:
                        return cms

                elif method == 'keyword' and location == 'header':
                    for keyword in keywords:
                        if keyword in headers:
                            return cms

                elif title is not None:
                    if method == 'keyword' and location == 'title':
                        found_keywords = all(keyword in title for keyword in keywords)
                        if found_keywords:
                            return cms
        return None

    def get_finger(self, res, content):
        """
        获取指纹数据
        :param res:response数据
        :param content: 识别到的title和icon_hash数据
        :return:json
        """
        title = content.get("title")
        icon_hash = content.get("icon_hash")
        headers = str(res.headers)
        cms = self._run_get_finger(title, icon_hash, headers, res)

        return cms


finger = GetFingerClass()
