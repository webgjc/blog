from flask import Flask,render_template,request,jsonify,make_response,send_from_directory
from bs4 import BeautifulSoup
import os
import sys
import io
from PIL import Image
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
import requests
import time
import random
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

app = Flask(__name__)
req = requests.Session()

@app.route("/",methods=["GET"])
def main():
    return render_template("main.html")

@app.route("/hack",methods=["POST"])
def hack():
    url = request.form.get("url")

    if url.find("-m.html")==-1:
        url = url.replace(".html","-m.html")
        imgdir = "static/"

    if url.find("-m.html")==-1:
        return jsonify({"sts":-1})
    else:
        imgdir = "static/"

    resp = req.get(url)

    soup=BeautifulSoup(resp.text,"lxml")

    title = soup.find_all("title")[0].text.replace(" ","").replace("/","")

    mp3 = soup.find_all("source")[0]["src"]

    picul = soup.find_all("ul",{"class":"swiper-wrapper"})[0]

    images = picul.find_all("img")

    fname_list = []

    for i in images:
        imgurl = req.get(i['src'])
        fname = ".".join(i['src'].split(".")[-2:])
        fname_list.append(fname)
        with open(imgdir+fname,"wb") as f:
            f.write(imgurl.content)
            f.close()
    
    f_pdf = "./static/"+str(int(random.random()*8999+1000))+".pdf"
    (w, h) = landscape(A4)
    c = canvas.Canvas(f_pdf, pagesize = (h,w))

    for file in fname_list:
        c.drawImage(imgdir+file,0,0,h,w)
        c.showPage()
        os.remove(imgdir+file)
    c.save()
    return jsonify({"sts":1,"msg":{"title":title,"pdf":"/pdf"+f_pdf[8:],"mp3":mp3}})
'''
@app.route("/pdf/<filename>")
def download(filename):
    #return send_from_directory("pdf", filename, as_attachment=True)
    file_name= filename
    response = make_response(send_from_directory('pdf/',file_name,as_attachment=True))
    response.headers["Content-Disposition"] = "attachment; filename={}".format(file_name.encode().decode('latin-1'))
    return response
'''
@app.route("/pdf/<filepath>", methods=['GET'])
def download_file(filepath):
    return app.send_static_file(filepath)

if __name__=="__main__":
    app.run("0.0.0.0",8888,debug=True)
    
