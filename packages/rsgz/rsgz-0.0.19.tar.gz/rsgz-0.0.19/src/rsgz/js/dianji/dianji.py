import re
from bs4 import BeautifulSoup


# 提取主标签
def get_main_tag(the_source):
    r"""
    寻找思路:正则表达式能匹配的</*> *部分就是主标签
    the_source = r'''<a href="https://www.wish.com/c/6352c1f192bffdf1c180a37b" target="_blank" ng-bind-html="item.title" class="ng-binding ng-scope">Top Winter Plus Size XS-8XL</a>'''
    get_main_tag(the_source)  # ['a', 'select', 'option', 'option', 'option']
    """

    if re.findall("<[a-zA-Z0-9]{1,20}", the_source):
        ele_list = re.findall("<[a-zA-Z0-9]{1,20}", the_source)
        ele_list = [i[1:] for i in ele_list]
        return ele_list

# 获取tag对象
def get_tag_obj(tag):
    r"""
    tag_list = get_main_tag(the_source)  # 将获取的字符串 标签列表  转换成tag对象  tag对象有很多的参数属性可以选择
    """

# 获取属性
def get_attr(the_source, more=None, parser=None):
    r"""
    parser = "html.parser"
    parser = "lxml.parser"

    获取标签的所有属性 根据属性获取对象
    the_source = r'''<a href="https://www.wish.com/c/6352c1f192bffdf1c180a37b" target="_blank" ng-bind-html="item.title" class="ng-binding ng-scope">Top Winter Plus Size XS-8XL</a>'''
    get_attr(the_source)

    <video class="" playsinline="true" x5-playsinline="true" webkit-playsinline="true" tabindex="2" mediatype="video"
    autoplay="" tsbrowser_force_max_size="true"><source class=""
    src="//v26-web.douyinvod.com/335eaae207c25daee6a2520734dc1237/63706d97/video/tos/cn/tos-cn-ve-15c001-alinc2/o4G2HoDllsWlbpIADeEeOYAInbAYeCTJJEONeU/?a=6383&amp;ch=5&amp;cr=3&amp;dr=0&amp;lr=all&amp;cd=0%7C0%7C0%7C3&amp;cv=1&amp;br=1611&amp;bt=1611&amp;cs=0&amp;ds=6&amp;ft=rVWEerwwZRLGsk~o1PDS6kFgAX1tGknH4S9eFqrHxFr12ni7t&amp;mime_type=video_mp4&amp;qs=4&amp;rc=Omc2ZWg0NTk3ODo8PGRmO0BpMzxucTY6ZjppZzMzNGkzM0BeMjZeMi4uNi4xLy5jNTAtYSMwZmhpcjRnLmhgLS1kLS9zcw%3D%3D&amp;l=202211131047500102081611013DAA5029" type=""><source class="" src="//v3-web.douyinvod.com/dea7409de1359db205b6b3678c696cb4/63706d97/video/tos/cn/tos-cn-ve-15c001-alinc2/o4G2HoDllsWlbpIADeEeOYAInbAYeCTJJEONeU/?a=6383&amp;ch=5&amp;cr=3&amp;dr=0&amp;lr=all&amp;cd=0%7C0%7C0%7C3&amp;cv=1&amp;br=1611&amp;bt=1611&amp;cs=0&amp;ds=6&amp;ft=rVWEerwwZRLGsk~o1PDS6kFgAX1tGknH4S9eFqrHxFr12ni7t&amp;mime_type=video_mp4&amp;qs=4&amp;rc=Omc2ZWg0NTk3ODo8PGRmO0BpMzxucTY6ZjppZzMzNGkzM0BeMjZeMi4uNi4xLy5jNTAtYSMwZmhpcjRnLmhgLS1kLS9zcw%3D%3D&amp;l=202211131047500102081611013DAA5029" type=""><source class="" src="//www.douyin.com/aweme/v1/play/?video_id=v0200fg10000cdkf17jc77u3lnkki930&amp;line=0&amp;file_id=083c8af9192745149612115eab935da7&amp;sign=c112973f3dabe6ad845fa5a31bfbaca6&amp;is_play_url=1&amp;source=PackSourceEnum_FEED&amp;aid=6383" type=""></video>
    """

    tag_list = get_main_tag(the_source)
    print(tag_list)

    soup = BeautifulSoup(the_source, "{}".format(parser))
    # print(soup.tag_list[0])


    for i in range(len(tag_list)):
        print("--------------------------------")
        if tag_list[i]=="select":
            tag = soup.select("select")[0]
        else:
            tag = eval("soup.{}".format(tag_list[i]))  # 标签
        # print(tag)
        print("标签名:", tag.name)

        # 全部属性
        try:
            print("全部属性:", tag.attrs)
        except:
            pass


        # 标签选择器 ------------------------------------------------------------------
        if more!=None:
            print('\033[1;34;40m标签选择器\033[0m')
            print("标签选择器:", r'var x = document.getElementsByTagName("{}");'.format(tag.name))
            print("文本:", r'var x = document.getElementsByTagName("{}")[0].innerHTML;'.format(tag.name))
            print("背景颜色:", r'var x = document.getElementsByTagName("{}")[0].style.backgroundColor= "coral";'.format(tag.name))
        else:
            print('\033[1;34;40m标签选择器\033[0m', r'var x = document.getElementsByTagName("{}");'.format(tag.name))

        # id选择器  ------------------------------------------------------------------
        try:
            if "id" in tag.attrs:
                if more != None:
                    pass
                else:
                    print('\033[1;34;40mID选择器\033[0m', r'var x = document.getElementById("{}");'.format(tag['id']))
        except:
            pass

        # class选择器  ------------------------------------------------------------------
        try:
            if "class" in tag.attrs:
                if more != None:
                    pass
                else:
                    print('\033[1;34;40mclass选择器\033[0m', r'var x = document.getElementsByClassName("{}");'.format(' '.join(tag['class'])))
        except:
            pass

        # name选择器 ------------------------------------------------------------------
        try:
            if "name" in tag.attrs:
                if more != None:
                    pass
                else:
                    print('\033[1;34;40mname选择器\033[0m', r'var x = document.getElementsByName("{}");'.format(tag['name']))
        except:
            pass


        # CSS选择器  ------------------------------------------------------------------
        try:
            if more != None:
                pass

            else:
                print('\033[1;34;40mcss选择器+tag\033[0m', r'var x = document.querySelectorAll("{}");'.format(tag.name))

            if 'class' in tag.attrs:
                print('\033[1;34;40mcss选择器+class\033[0m', r'var x = document.querySelectorAll("{}.{}");'.format(tag.name, '.'.join(tag['class'])))

            if 'id' in tag.attrs:
                print('\033[1;34;40mcss选择器+id\033[0m', r'var x = document.querySelectorAll("{}#{}");'.format(tag.name, tag['id']))


            tag_attrs_dict=tag.attrs.copy()

            try:
                del tag_attrs_dict['class']
            except:
                pass

            try:
                del tag_attrs_dict['id']
            except:
                pass

            # tag_attrs_dict.pop('class')
            # tag_attrs_dict.pop('id')

            key_list = list(tag_attrs_dict.keys())
            for k in range(len(key_list)):
                print('\033[1;34;40mcss选择器\033[0m', r'var x = document.querySelectorAll("{}[{}]");'.format(tag.name, key_list[k]))
                print('\033[1;34;40mcss选择器\033[0m', r'''var x = document.querySelectorAll('[{}="{}"]');'''.format(key_list[k], tag_attrs_dict[key_list[k]]))


            # 针对找到的元素列表 进行批量操作
            print("所有元素隐藏:", 'x.forEach(item=>{item.hidden=true})')

            # document.querySelectorAll(".start div #img>p")

        except:
            pass

# 定位元素
def find_ele(the_source=None, the_id=None, the_class=None, the_name=None, browser_xpath=None):
    r"""
    罗列简洁锁定元素的代码
    find_ele()
    """

    if the_id!=None:
        v_id_1 = r"""
document.getElementById("{}");
        """.format(the_id)
        print(v_id_1)
        pass

    if the_class!=None:
        v_class_1 = r"""
document.getElementsByClassName("{}");
                """.format(the_class)
        print(v_class_1)
        pass

    if the_name!=None:
        pass

    r"""
document.getElementsByClassName
document.getElementsByName
document.getElementsByTagName
document.getElementsByTagNameNS
document.getSelection
document.getRootNode
    """

    tips = r"""
源代码:{}
主标签:{}
class:{}
id:{}
简洁xpath:{}
浏览器xpath:{}
        """.format(the_source, get_main_tag(the_source), the_class, the_id, the_id,the_id)
    print(tips)
    pass

# 实现xpath点击元素
def x_path_click(xpath1, func_name, the_time, **vartuple):
    r"""
    实现xpath点击元素
    xpath 表示xpath路径
    func_name 给点击函数取一个名字
    the_time  多少秒后执行点击函数

    xpath1 = r"/html/body/div[8]/div/div/div/mg-box/div/div[1]/form/div[2]/table/thead/tr/th[3]/mg-widget-batch/div/div[1]/span/div[1]/div/div[2]/ng-include/ul/li[40]/div"
    vartuple = {'func_name1':'func_name1','func_name2':'func_name2','xpath2':'xpath2'}
    x_path_click(xpath1, func_name="click_yunfeimuban", the_time=2000, **vartuple)

    """
    func1 = r"""
// ---------------- script ----------------
var script = document.createElement('script');
script.src = "https://upcdn.b0.upaiyun.com/libs/jquery/jquery-2.0.2.min.js";
document.getElementsByTagName('head')[0].appendChild(script);
    """.format()

    func2 = r"""
// ---------------- 方式1 func+setTimeout ----------------
function {}(){{
    document.evaluate('{}', document).iterateNext().click()
}}

setTimeout(()=>{}(),{})
    """.format(func_name, xpath1, func_name, the_time)

    func3 = r"""
// ---------------- 方式2:$x(xpath) ----------------
// 适合放在函数外面
$x("{}")[0].click()
    """.format(xpath1)

    func4 = r"""
// ---------------- 方式3:回调函数 ----------------
function {}(callback){{
    document.evaluate('{}', document).iterateNext().click()
    callback();
}}

function {}(){{
    document.evaluate('{}', document).iterateNext().click()
}}

{}({});
    """.format(vartuple['func_name1'], xpath1,
               vartuple['func_name2'], vartuple['xpath2'],
               vartuple['func_name1'], vartuple['func_name2'])

    print(func1+func2+func3+func4)
    pass


if __name__ == '__main__':
    xpath1 = r"/html/body/div[8]/div/div/div/mg-box/div/div[1]/form/div[3]/button[1]"
    xpath2 = r""
    vartuple = {'func_name1':'func_name1', 'func_name2':'func_name2', 'xpath2':xpath2}
    # x_path_click(xpath1, func_name="click_yunfeimuban", the_time=2000, **vartuple)

    # ------------------------------------------
    the_source = r"""<a href="https://www.wish.com/c/6352c1f192bffdf1c180a37b" target="_blank" ng-bind-html="item.title" class="ng-binding ng-scope">Top Winter Plus Size XS-8XL</a>"""
    browser_xpath = r"""//*[@id="ngContainer"]/div/div[2]/div[3]/mg-box/div/div[1]/div[1]/table/tbody/tr[1]/td[5]/div/div[1]/a"""
    the_id = r""
    # find_ele(the_id=the_id, browser_xpath=browser_xpath, the_source=the_source)

    # ------------------------------------------
    the_source = \
r"""
<div data-v-73a8191d="" data-v-2190738e="" class="variation-edit-item">
"""
    # get_main_tag(the_source) # 获取主标签
    get_attr(the_source, parser="lxml")  # 获取属性


r"""
需要优化的方向：
简化xpath
<div class="read ng-binding ng-scope" ng-if="vm.searchText != '店铺搜索'" ng-hide="!vm.dropButton &amp;&amp; vm._current">店铺</div>
<div class="read ng-binding ng-scope" ng-if="vm.searchText != '店铺搜索'" ng-hide="!vm.dropButton &amp;&amp; vm._current">运费模板</div>

/html/body/div[9]/div/div/div/mg-box/div/div[1]/form/div[2]/table/thead/tr/th[3]/mg-widget-batch/div/div[1]/span/div[1]/div/div[1]/div

//*[@fieldid="pk_fct_ap_plan_table"]//*[contains(@class,"table-body")]//table//tr//*[@fieldid="planmoney"]//input

//*[@id="ngContainer"]//div/div[2]/div/div/div/div[2]/mg-box/div/div[1]/div[1]/table/tbody/tr[1]/td[4]/div/div[1]/div[1]

//*[@class="read ng-binding ng-scope"]/[contains(text(),'运费模板')]

//*[@id="result"]/div/p[2]
//*[@id="3"]/div/div[1]/h3/a

selector
#ngContainer > div > div:nth-child(3) > div > div > div > div.mui-container > mg-box > div > div:nth-child(1) > div.ng-scope.ng-isolate-scope > table > tbody > tr:nth-child(2) > td:nth-child(9) > div > div:nth-child(1) > span

定位更准确
"""