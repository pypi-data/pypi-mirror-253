import win32api
import win32con
import time

# direction参数为1表示向上滚动，-1表示向下滚动
# 接口文档：https://docs.microsoft.com/zh-cn/windows/win32/api/winuser/nf-winuser-mouse_event
def gun_top(n,t):
    for i in range(n):
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, 1*win32con.WHEEL_DELTA, 0)
        time.sleep(t)

def gun_down(n,t):
    for i in range(n):
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -1*win32con.WHEEL_DELTA, 0)
        time.sleep(t)

if __name__ == '__main__':
    gun_down(n=1,t=0.1)




































