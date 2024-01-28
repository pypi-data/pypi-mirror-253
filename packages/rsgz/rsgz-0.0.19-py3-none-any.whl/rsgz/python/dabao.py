import os
import subprocess

r"""
要使用API令牌，请执行以下操作:
1 设置用户名为 __token__
2 将密码设置为令牌值，包括py pi-前缀

twine upload -u USERNAME
https://twine.readthedocs.io/en/stable/#entering-credentials
https://pypi.org/help/#apitoken
https://pypi.org/manage/account/  添加api令牌
pip install build==1.0.3
pip install twine==4.0.2
python -m build
"""

username = "__token__"
password = "pypi-AgEIcHlwaS5vcmcCJDM3ZTU2ZGYzLTZmNjQtNDRlYS04YTBhLTNjNmIyNmEyNzY4ZAACKlszLCJiNWNkMGY5ZS0wYjkwLTQ0MzAtOGNjZC05NjJmMzA4MDY0YmQiXQAABiAHjNEuEFXLSoIrHGCSFLJJaCcxPzg-_WnHSSOzBOdHIw"

def dabao():
    pro_dir = str(input("请输入pyproject.toml文件同级目录："))
    pan_fu = pro_dir.split(os.sep)[0]

    dabao_str = r"""
执行了以下命令：
{}
cd {}

第二步：
py -m build
python3.7 -m build
python -m build

第三步：
twine upload dist/*
    """.format(pan_fu, pro_dir)

    # os.system("start cmd")
    # 这种写法 输入账号之后 密码无法输入 pycharm发现的问题
    os.system("cmd /c {} & cd {} & python -m build & twine upload -u {} -p {} dist/* ".format(pan_fu,pro_dir,username,password))

    # 只是进行打包
    # os.system("cmd /c {} & cd {} & python -m build".format(pan_fu,pro_dir))
    # os.system('cmd /c {} & cd {} & twine upload -u username -p password dist/*  -r pypi'.format(pan_fu,pro_dir))

    # 打开cmd窗口并执行命令
    print(dabao_str)

dabao()