
def del_head_end_col(code):
    for id,x in enumerate(code):
        if x == '\n':
            # print(id,x)
            print("有空行！！！")
    pass

code=r"""
def ppp():
    cmb_str = lambda s1,s2:"{}{}".format(s1.upper(), s2.upper())
"""

print(del_head_end_col(code))