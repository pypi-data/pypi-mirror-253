import io
import os
import setuptools

current_dir = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(current_dir, "README.md"), encoding="utf-8") as fd:
    desc = fd.read()

setuptools.setup(
    name="fingerscan",
    license='',
    version="1.2.0",
    long_description=desc,
    long_description_content_type="text/markdown",
    description="指纹识别开发测试版本",
    author="zhizhuo",
    author_email="zhizhuoshuma@163.com",
    url='https://github.com/expzhizhuo',
    # 定义入口点，即命令行脚本
    entry_points={
        'console_scripts': [
            'fingerscan=fingerscan.fingerscan:main',
        ],
    },
    package_data={"fingerscan": ["*", "export/config/*"]},
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        "requests",
        "colorama",
        "mmh3",
        "urllib3",
        "pyfiglet",
        "termcolor",
        "openpyxl",
        "poc-tool",
        "alive-progress",
        "pyOpenSSL",
        "beautifulsoup4"
    ],
    python_requires=">=3.8",
)
