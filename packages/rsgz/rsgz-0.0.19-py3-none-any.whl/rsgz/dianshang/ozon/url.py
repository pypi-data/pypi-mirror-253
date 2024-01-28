import os,re

a = r"""
"\\R1\r1\新泳衣\泳衣所有款\泳衣新款1130\8258-1\purple5.jpg"
"\\R1\r1\新泳衣\泳衣所有款\泳衣新款1130\8258-1\black5.jpg"
"\\R1\r1\新泳衣\泳衣所有款\泳衣新款1130\8258-1\blue5.jpg"
"\\R1\r1\新泳衣\泳衣所有款\泳衣新款1130\8258-1\cyan5.jpg"
"""
a1=a.replace('"','').replace(r"\\R1\r1\新泳衣\泳衣所有款\泳衣新款1130", '').split(os.sep)


aa=[]
for p in a1:
    if "." in p:
        p1=re.findall(r"[a-zA-Z]+", p)[0]
        aa.append(p1.replace("\n",'').replace('jpeg','').replace('png','').replace('jpg',''))
aaa=','.join(aa)
# print("'{}'.split(',')".format(aaa))
# print(a.replace("\n",","))

def g(url, l):
    u2_l=[]
    u1 = url[60:].split("/")  # '8258', 'black.png'
    for color in l:
        u2= url[0:60]+u1[0]+"/"+color+"/1.png"
        u2_l.append(u2)

    for u in u2_l:
        # print(u)
        pass
    return u2_l

if __name__ == '__main__':
    pass
    # for i in g(url=r"https://rsgz001.oss-cn-shenzhen.aliyuncs.com/mangguo/yongyi/8258/black.jpg", l="black,red,green,blue".split(',')):
    #     print(i)
