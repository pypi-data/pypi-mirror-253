import win32api, pyautogui
import time
import win32clipboard as w
import win32con
import pyperclip

# 简单属性
kuaijiejian=pyautogui.hotkey

# 获取粘贴板
def get_text():
    return pyperclip.paste()

# 设置粘贴板
def set_text(text):
    pyperclip.copy(text)

def zhantie(text):
    set_text(text)
    s = get_text()
    pyautogui.hotkey('ctrl', 'v')

def PressOnce(x):  # 模拟键盘输入一个按键的值，键码: x
    win32api.keybd_event(x, 0, 0, 0)

def open_web1(url):
    pyautogui.hotkey('ctrl', 't')
    pyautogui.typewrite(url, interval=0.01)
    time.sleep(0.2)
    enter()
    time.sleep(0.2)
    enter()

# 这是第二种方式
def open_web2(url):
    pyautogui.hotkey('ctrl', 't')
    zhantie(url)
    time.sleep(0.2)
    enter()

def enter():
    PressOnce(13)  # Enter


