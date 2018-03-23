#coding:utf-8
#author:ganjiacheng
#contact:qq 935669873
from PIL import Image,ImageFile
import win32api,win32con,win32gui  
import re,os  
import requests
from io import BytesIO
from bs4 import BeautifulSoup
import tkinter
import random
import math
import time
import re
from ctypes import *
import pyHook
import pythoncom
import threading
ImageFile.LOAD_TRUNCATED_IMAGES = True

def set_wallpaper_from_bmp(bmp_path):  
    #打开指定注册表路径  
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)  
    #最后的参数:2拉伸,0居中,6适应,10填充,0平铺  
    win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "2")  
    #最后的参数:1表示平铺,拉伸居中等都是0  
    win32api.RegSetValueEx(reg_key, "TileWallpaper", 0, win32con.REG_SZ, "0")  
    #刷新桌面  
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,bmp_path, win32con.SPIF_SENDWININICHANGE)  
  
def set_wallpaper(bgimg):  
    #把图片格式统一转换成bmp格式,并放在源图片的同一目录 
    if bgimg!=0:
        new_bmp_path="C:/backgroundPicture/wallpaper.bmp"
        bmpImage = Image.open(BytesIO(bgimg))
        bmpImage.save(new_bmp_path, "BMP")  
        set_wallpaper_from_bmp(new_bmp_path)  
    else:
        pass

def getPicurl():
    req=requests.Session()
    '''resp=req.get("https://bing.ioliu.cn/?p=1")
    soup=BeautifulSoup(resp.text,"lxml")
    pageall=soup.find_all("span")[-1].get_text()
    maxpage=int(pageall.split("/")[1].strip())'''
    maxpage=57
    ran=math.floor(random.random()*maxpage)+1
    resp1=req.get("https://bing.ioliu.cn?p="+str(ran))
    soup1=BeautifulSoup(resp1.text,"lxml")
    allimg=soup1.find_all("img")
    ran1=math.floor(random.random()*len(allimg))
    resp2=req.get("https://bing.ioliu.cn"+allimg[ran1].next_sibling['href'])
    resp2.encode='utf-8'
    url=re.findall(r'data-progressive="(.*?)"',resp2.text)[0]
    headers={
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate",
        "Host":"h1.ioliu.cn",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
    }
    image=req.get(url,headers=headers)
    return image.content

def inputint():
    global t
    try:
        t = int(var.get().strip())
    except:
        t = 30
    root.destroy()

def onKeyboardEvent(event):
    global lt
    if event.Ascii==96:
        if time.time()-lt<2:
            bgimg=getPicurl()
            set_wallpaper(bgimg)
        else:
            lt=time.time()
    return True

def task0():
    hm = pyHook.HookManager()
    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()

def task1():
    global t
    while True:
        bgimg=getPicurl()
        set_wallpaper(bgimg)
        time.sleep(int(t*60))

if __name__ == '__main__':  
    t=30
    lt=0
    if not os.path.exists('C:/backgroundPicture/'):
        os.mkdir("C:/backgroundPicture/")
    root = tkinter.Tk(className='请输入间隔时间(按分钟计)')  # 弹出框框名
    root.geometry('350x60')     # 设置弹出框的大小 w x h
    var = tkinter.StringVar()   # 这即是输入框中的内容
    var.set(30) # 通过var.get()/var.set() 来 获取/设置var的值
    entry1 = tkinter.Entry(root, textvariable=var)  # 设置"文本变量"为var
    entry1.pack()   # 将entry"打上去"
    btn1 = tkinter.Button(root, text='确认', command=inputint)     # 按下此按钮(Input), 触发inputint函数
    btn1.pack(side='bottom')
    root.mainloop()
    threads = []
    t1 = threading.Thread(target=task0)
    threads.append(t1)
    t0 = threading.Thread(target=task1)
    threads.append(t0)
    for i in range(2):
        threads[i].start()
    for i in range(2):
        threads[i].join()
    # 按钮定位
    