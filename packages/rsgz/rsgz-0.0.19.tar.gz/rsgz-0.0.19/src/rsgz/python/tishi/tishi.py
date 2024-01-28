

def tishi(t):
    s1 = r"""a = int(input('请输入一个数:'))"""
    s2 = r"""a, b = b, a"""
    s3 = r"""li.append(n if n%2==0 else 0)"""
    s4 = r"""maxnum=a if a>b else b"""
    s5 = r"""
x = 12
x = x + 1 if x % 2 == 0 else x
print(x)
    """
    s6 = r"""
def fn(n):
    return n if n<2 else fn(n-1)+fn(n-2)
print(fn(10))  # 55
    """
    s7 = r"""
cmb_str = lambda s1,s2:"{}{}".format(s1.upper(), s2.upper())
    """
    # ===================================================================
    ss=[
        ["输入数字", s1],
        ["交换数字", s2],
        ["三目运算符", s3],
        ["比较大小", s4],
        ["偶数加1，奇数不变", s5],
        ["斐波那契函数", s6],
        ["两个字符串拼接转化成大写", s7],
    ]

    flag=0
    for yuju in ss:
        if t==yuju[0]:
            print(yuju[1])
            flag = 1
    if flag==0:
        print("查询的数据未记录!!! 请参考相似记录")
        for yuju in ss:
            if t in yuju[0]:
                print(yuju[0])
if __name__ == '__main__':
    tishi(t="12")