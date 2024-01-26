"""
@Project ：指纹识别 
@File    ：get_icp.py
@IDE     ：PyCharm 
@Author  ：zhizhuo
@Date    ：2024/1/14 18:38 
"""
import requests
from bs4 import BeautifulSoup


class GetIcpInfo(object):
    """
    获取站点的icp备案信息
    """

    def __init__(self, body: str):
        """
        初始化配置信息
        """
        self.body = body
        self.forbidden_strings = ['.js', '.html', '.txt', '.css', '/', 'script', '<', '>']

    # def _get_icp_info(self):
    #     """
    #     获取备案信息
    #     :return:icp备案信息
    #     """
    #     match = re.findall(r'href=".*?//beian.miit.gov.cn.*?>(.*?)</a>', self.body)
    #     return match[0] if match else None

    def _get_icp_info(self):
        """
        获取ICP备案信息
        :return:ICP备案信息
        """
        search_tags = ["script", "css", "js", "div", "<", ">", "div"]
        if any(tag in self.body for tag in search_tags):
            soup = BeautifulSoup(self.body, 'html.parser')
            icp_info = soup.find(string=lambda text: text and "ICP" in text)
            results = icp_info.strip() if icp_info else None
            if results:
                if len(results) > 50 or any(fs in results for fs in self.forbidden_strings):
                    return None
                split_result = results.split("：", 1)
                if len(split_result) == 2:
                    return split_result[1]
        else:
            results = None
        return results

    def run(self):
        """
        主入口函数
        :return:icp备案信息
        """
        return self._get_icp_info()


if __name__ == '__main__':
    headers = {
        'Accept': 'application/x-shockwave-flash, image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, '
                  'application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*',
        'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Connection': 'close'
    }
    url = 'https://www.xinruiiot.com/'
    res = requests.get(url=url, headers=headers)
    # print(res.text)
    res.encoding = res.apparent_encoding
    result = GetIcpInfo(body=res.text).run()
    print('ICP->', result)
    exit()

# import requests
#
#
# def get_icp_info(url):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         soup = BeautifulSoup(response.text, 'html.parser')
#         icp_info = soup.find(string=lambda text: text and "ICP" in text)
#         return icp_info.strip() if icp_info else "No ICP information found"
#     except requests.RequestException as e:
#         return str(e)
#
#
# # if __name__ == "__main__":
# #     test_url = "https://www.mi.com/"  # Replace with a real URL to test
# #     print('ICp->', get_icp_info(test_url))
#
# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
#
#
# def fetch_and_parse_icp(url):
#     print(1)
#     # Initialize a headless browser
#     options = webdriver.ChromeOptions()
#     options.add_argument('headless')
#     print(1)
#     driver = webdriver.Chrome(options=options)
#     print(1)
#
#     # Fetch the page
#     driver.get(url)
#     print(1)
#
#     # Render the page as a browser would
#     rendered_html = driver.page_source
#     print(1)
#     # print(rendered_html)
#     driver.quit()
#
#     # Parse the HTML for ICP information
#     soup = BeautifulSoup(rendered_html, 'html.parser')
#     print(soup)
#     icp_info = soup.find(string=lambda text: text and "ICP" in text)
#
#     return icp_info
#
#
# # Test case
# if __name__ == "__main__":
#     import time
#
#     test_url = 'https://fanyi.youdao.com/'
#     time_start = time.time()
#     print(fetch_and_parse_icp(test_url))
#     time_end = time.time()
#     time_total = time_end - time_start
#     print(f'总共用时{time_total}')
