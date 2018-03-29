#coding:utf-8
import requests
from bs4 import BeautifulSoup
import os
import sys
import io
from PIL import Image
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
import time
import random
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

#输入弹琴吧所需琴谱的网址
#把网址变成手机访问的网址
req = requests.Session()
url=""
#url = "http://www.tan8.com/yuepu-58546.html"
state=True

while state:
    url = input("输入弹琴吧钢琴曲网址：\n")
    if url.find("-m.html")==-1:
        url = url.replace(".html","-m.html")
        imgdir = "tmpimgtan8/"

    if url.find("-m.html")==-1:
        print("请输入正确网址")
    else:
        imgdir = "tmpimgtan8/"
        state=False

if not os.path.exists(imgdir):
    os.mkdir("tmpimgtan8")
#爬下来解析出mp3，图片地址
#保存MP3，图片
resp = req.get(url)

soup=BeautifulSoup(resp.text,"lxml")

#windows可以用这个中文名做文件名
title = soup.find_all("title")[0].text.replace(" ","").replace("/","")
#linux用下面的随机数做文件名
#title = str(int(random.random()*8999)+1000)

mp3 = soup.find_all("source")[0]["src"]
mreq = req.get(mp3)
print(title)
with open(title+".mp3","wb") as f:
    f.write(mreq.content)
    f.close()

picul = soup.find_all("ul",{"class":"swiper-wrapper"})[0]

images = picul.find_all("img")

for i in images:
    imgurl = req.get(i['src'])
    with open(imgdir+".".join(i['src'].split(".")[-2:]),"wb") as f:
        f.write(imgurl.content)
        f.close()

files=os.listdir(imgdir)

if "Thumbs.db" in files:
    files.remove("Thumbs.db")
#把图片连接成pdf
f_pdf = title+".pdf"
(w, h) = landscape(A4)
c = canvas.Canvas(f_pdf, pagesize = (h,w))

for file in files:
    c.drawImage(imgdir+file,0,0,h,w)
    c.showPage()
    os.remove(imgdir+file)
c.save()
try:
    os.rmdir("tmpimgtan8")
except:
    print("请手动删除 tmpimgtan8")