
r"""
这个模块就是将所有的克重的运费算出来 然后图形化界面显示出来 找出最合理的
"""

def print_wuliu(guojia=None, weight=None):

    if guojia=="马来西亚":
        # zone kv
        if weight<800:
            if weight%10==0:  # 能整除
                print(7.6+(weight/10)*0.24)
            else:
                # print(7.6 + (weight//10+1) * 0.24)  # 加一法
                print(7.6 + (weight/10) * 0.24) # 除尽法

        if weight>800:
            if weight%10==0:  # 能整除
                print(7.6 + (weight / 10) * 0.24)

print_wuliu(guojia="马来西亚", weight=788)