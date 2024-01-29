"""
@Project ：指纹识别 
@File    ：fingerscan.py
@IDE     ：PyCharm 
@Author  ：zhizhuo
@Date    ：2023/12/18 14:33 
"""
import json
import os
from datetime import datetime

from util.agent import agent
from pyfiglet import Figlet
from termcolor import cprint
import colorama
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from alive_progress import alive_bar
from poc_tool.log import log, LOGGER, LoggingLevel
from poc_tool.tools import tools
from export.output_file import get_excel

# 解决cmd样式问题
colorama.init(autoreset=True)
# 多线程操作
max_threads = 50


def write_file(file_name, content):
    """
    写入文件
    :param file_name:
    :param content:
    :return:
    """
    current_path = os.getcwd()
    if file_name is None:
        file_name = f"result_{datetime.now().strftime('%Y%m%d%H%M')}{tools.get_random_num(5)}.xlsx"
    if file_name and file_name.split(".")[-1] != "xlsx":
        log.error("异常文件类型，目前仅支持xlsx文件类型")
        return
    file_content_io = get_excel(content)
    with open(file_name, 'wb') as f:
        f.write(file_content_io)
    log.success(f"结果保存成功，已保存到文件{current_path}/{file_name}中")


def open_file(file_path):
    """
    打开文件
    :param file_path:
    :return:
    """
    return open('{}'.format(file_path), encoding='utf8').read().splitlines()


def finger_run(url, file_path):
    """
    主扫描函数
    :param url:url地址
    :param file_path:file地址
    :return:json
    """
    log.info(f"开始指纹扫描")
    result_data = []
    if url is None:
        urlfile = open_file(file_path)
    else:
        urlfile = ['{}'.format(url)]
    log.info(f"需要扫描{len(urlfile)}个资产")
    with alive_bar(len(urlfile)) as bar:
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            futures = []
            for host in urlfile:
                futures.append(executor.submit(agent(url=host).run))
            for future in as_completed(futures):
                res = future.result()
                bar()  # 更新进度
                try:
                    res_json = json.loads(res)
                except json.JSONDecodeError:
                    log.error(f"JSON解析失败: {res}")
                    continue
                for i in res_json:
                    cms = i.get("cms")
                    title = i.get("title")
                    status_code = i.get("status_code")
                    is_cdn = "是" if i.get("is_cdn", {}).get("is_cdn") else "否"
                    print(f'地址:{i.get("url")}\t指纹:{cms}\ttitle:{title}\t状态码:{status_code}\t是否使用CDN:{is_cdn}')
                    new_object = dict(host=i.get("host"), url=i.get("url"), scheme=i.get("scheme"),
                                      cms=i.get("cms"), title=i.get("title"),
                                      status_code=i.get("status_code"),
                                      redirect_num=i.get("redirect_num"), server=i.get("server"),
                                      is_cdn=i.get("is_cdn").get("is_cdn"),
                                      cdn_ip_list=i.get("is_cdn").get("ip_list"),
                                      icon_hash=i.get("icon_hash"),
                                      cert=i.get("cert"))
                    result_data.append(new_object)
    return result_data


def finger_scan_main(url, file_path, file_name):
    """
    主运行函数
    :param url:url地址
    :param file_path:file地址
    :param file_name:结果输出文件名字
    :return:json
    """
    result = finger_run(url, file_path)
    log.info(f"扫描完成，进行结果保存")
    if len(result) > 0:
        write_file(file_name, result)


def main():
    """
    程序的主入口
    :return:
    """
    cmd_output()


def cmd_output():
    global max_threads
    f = Figlet(font="slant", width=1500)
    cprint(f.renderText('''Finger Scan Dev Test Version
        by zhizhuo'''), "green")
    parser = argparse.ArgumentParser(
        description='''
        Finger Scan Dev Test Version
        by zhizhuo
        ''')
    parser.add_argument('-u', '-url', dest="url", type=str,
                        help='单个url检测，输入样例http://www.baidu.com', required=False)
    parser.add_argument('-f', '-file', dest="url_file", nargs='?', type=str,
                        help='多个url检测，以txt文件形式存储,文件中的url格式为http://www.baidu.com或者www.baidu.com',
                        required=False)
    parser.add_argument('-t', '-T', dest="threads", type=int,
                        help='线程数量，默认是50线程', required=False)
    parser.add_argument('-o', '-output', dest="output", nargs='?', type=str,
                        help='结果输出文件', required=False)
    parser.add_argument('-d', '-debug', dest="debug", default="debug", nargs='?', type=str,
                        help='开启debug模式', required=False)
    url_arg = parser.parse_args().url
    file_arg = parser.parse_args().url_file
    threads_arg = parser.parse_args().threads
    outfile_arg = parser.parse_args().output
    debug_arg = parser.parse_args().debug
    if debug_arg != "debug":
        LOGGER.setLevel(LoggingLevel.DEBUG)
    if threads_arg is not None:
        max_threads = int(threads_arg)
    if file_arg is not None or url_arg is not None:
        finger_scan_main(url_arg, file_arg, outfile_arg)
    else:
        print("参数错误，请使用命令-h查看命令使用帮助 --by zhizhuo")


if __name__ == '__main__':
    main()
