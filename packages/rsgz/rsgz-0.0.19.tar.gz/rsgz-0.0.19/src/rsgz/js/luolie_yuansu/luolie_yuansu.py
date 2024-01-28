import re

def luolie_yuansu(path_start, path_end):
    print("首行路径:", path_start)
    print("末尾路径:", path_end)

    # print('\n')
    # 先将左边相同的找出来
    comment = ''
    break_i= 0 # 中断的坐标
    for i in range(len(path_start)):
        if path_start[i]==path_end[i]:
            # print(path_start[i], end="")
            comment = comment+path_start[i]
        else:
            break_i = i
            # comment = comment[0:-2]
            break

    # 碰到最后一个是数字 倒数第二个是[  就将数字舍去
    if comment[-1].isalnum() and comment[-2]=='[':
        comment=comment[0:-2]   # ...div/ul/li[

    # print("---", comment)  # --- //*[@id="tsf"]/div[1]/div[1]/div[3]/div[2]/div[2]/div[1]/div/ul/li
    # 右边 相同部分 找出来
    new_path_start1 = path_start[break_i-2:]  # [1]/div/div[2]/div[1]/span
    start_index = new_path_start1.find(']')+1
    new_path_start2 = new_path_start1[start_index:]  # /div/div[2]/div[1]/span
    # 提取第一个[]中的数字
    start_i = re.findall(r"\w+", new_path_start1)[0]
    # print("---", new_path_start2, start_i)  # --- /div/div[2]/div[1]/span 1


    new_path_end1 = path_end[break_i-2:]  # [10]/div/div[2]/div[1]/span
    end_index = new_path_end1.find(']') + 1
    new_path_end2 = new_path_end1[end_index:] # /div/div[2]/div[1]/span
    end_i = re.findall(r"\w+", new_path_end1)[0]
    # print("---", new_path_end2, end_i)  # --- /div/div[2]/div[1]/span 10

    if new_path_start2!=new_path_end2:
        print('逻辑有缺陷!!!')


    new_xpath = comment+'['+"'+i+'"+']'+new_path_end2
    all = ''
    yuansu = \
r"""----------------------------
all=''
for(var i={};i<={};i++){{
    txt = $x('{}')[0].textContent+"\n"
    all = txt+all 
}}
console.log(all)
    """.format(start_i, end_i, new_xpath)
    print(yuansu)

if __name__ == '__main__':
    path_start = r'//*[@id="mtsku-list"]/div[1]/div[4]/div[1]/div/div/div[2]/table/tbody/tr[1]/td[2]/div/div/div[2]/div[2]/div'
    path_end = r'//*[@id="mtsku-list"]/div[1]/div[4]/div[1]/div/div/div[2]/table/tbody/tr[48]/td[2]/div/div/div[2]/div[2]/div'
    luolie_yuansu(path_start, path_end)
