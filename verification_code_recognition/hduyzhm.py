import requests
from PIL import Image
from io import BytesIO
from threading import Thread
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
class Mythread(Thread):
    def __init__(self,num):
        Thread.__init__(self)
        self.num=num
    def run(self):
        while True:  
            req = requests.get("http://jxgl.hdu.edu.cn/CheckCode.aspx",headers=headers)
            im=Image.open(BytesIO(req.content))
            im.save("croptest/"+str(self.num)+".png")
threads=[]
for j in range(10):
    for i in range(10):
        t=Mythread(i+10*j)
        t.start()
        print(i+10*j)
