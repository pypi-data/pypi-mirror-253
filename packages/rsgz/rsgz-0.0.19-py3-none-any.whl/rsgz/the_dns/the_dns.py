import dns.resolver


def yuming_to_ip(yuming):
    r"""
    域名转化为IP
    yuming_list = "baidu.com rsgz.top www.rsgz.top".split(" ")
    for yuming in yuming_list:
        yuming_to_ip(yuming)
    -----------------------------
    baidu.com--> 110.242.68.66
    baidu.com--> 39.156.66.10
    rsgz.top--> 113.96.179.225
    www.rsgz.top--> 113.96.179.223

    """
    res = dns.resolver.Resolver(configure=False)
    res.nameservers = [ '8.8.8.8', '2001:4860:4860::8888','8.8.4.4', '2001:4860:4860::8844' ]

    r = res.resolve('{}'.format(yuming), 'a')
    for i in r:
        print("{}-->".format(yuming), i)



if __name__ == '__main__':
    pass