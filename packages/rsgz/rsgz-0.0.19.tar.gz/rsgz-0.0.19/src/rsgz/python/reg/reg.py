import re

r"""
此模块 帮助快速完成Python版本正则表达式的书写
"""


def print_reg(str):
    r"""
    根据你传进的字符串参数 快速猜测 你需要的多种正则表达式
    """
    # print("1 原字符串：{}".format(str))

    # 2 如果存在英文 ----------------------------------
    if re.findall(r"[a-zA-Z]", str):
        tips = \
r"""
2 存在英文:{}
{}  # {}
{}  # {}
{}  # {}
{}  # {}
{}  # {}
{}  # {}
{}  # {}""".format(
'r"[a-zA-Z]"',
're.findall(r"[a-z]", str)', re.findall("[a-z]", str),
're.findall(r"[A-Z]", str)', re.findall("[A-Z]", str),
're.findall(r"[a-zA-Z]", str)', re.findall("[a-zA-Z]", str),
're.findall(r"[a-zA-Z]{1,2}", str)', re.findall("[a-zA-Z]{1,2}", str),
're.findall(r"[a-zA-Z]?", str)', re.findall("[a-zA-Z]?", str),
're.findall(r"[a-zA-Z]+", str)', re.findall("[a-zA-Z]+", str),
're.findall(r"[a-zA-Z]*", str)', re.findall("[a-zA-Z]*", str),
                   )
        print(tips)


    # 3 如果存在数字 ----------------------------------
    if re.findall(r"[0-9]", str):
        tips = \
r"""
3 存在数字:{}
{}  # {}
{}  # {}
{}  # {}
{}  # {}
{}  # {}""".format(
'r"[0-9]"',
're.findall("[0-9]", str)', re.findall("[0-9]", str),
're.findall("[0-9]{1,2}", str)', re.findall("[0-9]{1,2}", str),
're.findall("[0-9]?", str)', re.findall("[0-9]?", str),
're.findall("[0-9]+", str)', re.findall("[0-9]+", str),
're.findall("[0-9]*", str)', re.findall("[0-9]*", str),
                   )
        print(tips)


    # 4 存在英文和数字 ----------------------------------
    if re.findall(r"[0-9]", str) and re.findall(r"[a-zA-Z]", str):
        sentences1 = 're.findall(r"[0-9a-zA-Z]", str)'
        sentences2 = 're.findall(r"[0-9a-zA-Z]{1,2}", str)'
        sentences2_1 = 're.findall(r"[0-9a-zA-Z]{15,50}", str)'
        sentences3 = 're.findall(r"[0-9a-zA-Z]?", str)'
        sentences4 = 're.findall(r"[0-9a-zA-Z]+", str)'
        sentences5 = 're.findall(r"[0-9a-zA-Z]*", str)'

        tips = \
r"""
4 存在英文和数字:{}
{}  # {}
{}  # {}
{}  # {}
{}  # {}
{}  # {}
{}  # {}""".format(
'r"[0-9a-zA-Z]"',
sentences1, eval(sentences1),
sentences2, eval(sentences2),
sentences2_1, eval(sentences2_1),
sentences3, eval(sentences3),
sentences4, eval(sentences4),
sentences5, eval(sentences5),
                    )
        print(tips)


    # 5 如果存在中文 ----------------------------------
    if re.findall(r"[\u4e00-\u9fa5]", str):
        sentences1 = 're.findall(r"[\\u4e00-\\u9fa5]", str)'
        sentences2 = 're.findall(r"[\\u4e00-\\u9fa5]{1,2}", str)'
        sentences3 = 're.findall(r"[\\u4e00-\\u9fa5]?", str)'
        sentences4 = 're.findall(r"[\\u4e00-\\u9fa5]+", str)'
        sentences5 = 're.findall(r"[\\u4e00-\\u9fa5]*", str)'

        tips = \
r"""
5 存在中文:{}
{}  # {}
{}  # {}
{}  # {}
{}  # {}
{}  # {}""".format(
'r"[\\u4e00-\\u9fa5]"',
sentences1, eval(sentences1),
sentences2, eval(sentences2),
sentences3, eval(sentences3),
sentences4, eval(sentences4),
sentences5, eval(sentences5),)
        print(tips)


    # x 更多匹配 ----------------------------------
    sentences1 = r're.findall(r"[-+]", str)'
    sentences2 = r're.findall(r"[:]", str)'
    sentences3 = r're.findall(r"[/]", str)'
    sentences4 = r're.findall(r"[*]", str)'
    sentences5 = r're.findall(r"[%&]", str)'
    sentences6 = r're.findall(r"[$^]", str)'
    sentences7 = r're.findall(r"[#@!]", str)'
    sentences8 = r're.findall(r"[\\]", str)'
    sentences9 = r're.findall(r"[\"]", str)'
    sentences10 = r're.findall(r"[\']", str)'
    sentences11 = r're.findall(r"[_]", str)'
    sentences12 = r're.findall(r"http[s]?://", str)'
    sentences13 = r're.findall(r"[</>]", str)'
    sentences14 = r're.findall(r"([a-zA-Z]|[0-9])", str)'
    sentences15 = r're.findall(r"([a-zA-Z]|[0-9])+", str)'
    sentences16 = r're.findall(r"([0-9])+", str)'
    tips = \
r"""
x 更多匹配
{}  # {}
{}  # {}
{}  # {}
{}  # {}
{}  # {}
{}  # {}
{}  # {}
{}  # {}
{}  # {}
{}  # {}
{}  # {}
{}  # {}
{}  # {}
{}  # {}
{}  # {}
{}  # {}""".format(
sentences1, eval(sentences1),
sentences2, eval(sentences2),
sentences3, eval(sentences3),
sentences4, eval(sentences4),
sentences5, eval(sentences5),
sentences6, eval(sentences6),
sentences7, eval(sentences7),
sentences8, eval(sentences8),
sentences9, eval(sentences9),
sentences10, eval(sentences10),
sentences11, eval(sentences11),
sentences12, eval(sentences12),
sentences13, eval(sentences13),
sentences14, eval(sentences14),
sentences15, eval(sentences15),
sentences16, eval(sentences16),
                  )
    print(tips)



if __name__ == '__main__':
    import more_match_v3
    str = more_match_v3.str
    print_reg(str)
