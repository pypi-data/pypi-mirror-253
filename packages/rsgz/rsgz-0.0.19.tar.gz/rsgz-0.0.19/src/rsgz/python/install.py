import os

def install():
    python_module = input("模块名:")
    os.system("pip install {} -i https://pypi.tuna.tsinghua.edu.cn/simple".format(python_module))

if __name__ == '__main__':
    install()