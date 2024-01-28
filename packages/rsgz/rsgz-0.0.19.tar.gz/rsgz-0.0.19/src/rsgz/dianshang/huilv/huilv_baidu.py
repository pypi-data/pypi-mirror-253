import requests
from lxml import etree
from lxml.cssselect import CSSSelector

r"""
pip3.7 install lxml -i http://pypi.douban.com/simple/
pip3.7 install cssselect
"""


headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
}

url_lubu = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=%E5%8D%A2%E5%B8%83%E6%B1%87%E7%8E%87%E6%8D%A2%E7%AE%97"


def Get_huilv(url, headers1):
    res = requests.get(url=url, headers=headers1, timeout=2)
    print(res)
    # print(res.status_code)#打印状态码
    html = etree.HTML(res.text)
    result = html.cssselect('.op_exrate_result div:nth-of-type(1)')
    print(result)

Get_huilv(url=url_lubu, headers1=headers)