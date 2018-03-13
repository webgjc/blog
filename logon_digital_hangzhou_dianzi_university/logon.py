import requests
import re
import hashlib

#先访问一次登录网站得到lt（lt后面必须，且一次性使用）
def getHduCookie():
    resp=requests.get('http://cas.hdu.edu.cn/cas/login')
    m = re.search(r'name=\"lt\" value=(.*?) />', resp.text)
    lt=m.group()[17:-4]
    return lt

#模拟登陆用户名为学号，密码为md5加密后的密码，返回跳转链接
def simLogin(lt):
    password=hashlib.md5(psd.encode('utf-8')).hexdigest()
    params={
        'encodedService':'http%3a%2f%2fi.hdu.edu.cn%2fdcp%2findex.jsp',
        'service':'http://i.hdu.edu.cn/dcp/index.jsp',
        'username':xh,
        'password':password,
        'lt':lt
    }
    resp=requests.post('http://cas.hdu.edu.cn/cas/login?service=http://jxgl.hdu.edu.cn/index.aspx',params=params)
    m=re.search(r'href="(.*?)"',resp.text)
    return m.group()[6:-1]

#去临时链接获取一次cookie并保存请求
def jxglPage(url):
    req=requests.Session()
    resp0=req.get(url)
    req.headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Referer':'http://jxgl.hdu.edu.cn/xf_xsqxxxk.aspx?xh='+xh+'&xm=%25%5cB8%25%5cCA%25%5cBC%25%5cD2%25%5cB3%25%5cC7&gnmkdm=N121113',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type':'application/x-www-form-urlencoded',
    }
    return req

#这里的例子是获取选课列表
def classList(req):
    data=''#这里是post的一大串字符，可从浏览器获取
    url='http://jxgl.hdu.edu.cn/xf_xsqxxxk.aspx?xh='+xh+'&xm=%25%5cB8%25%5cCA%25%5cBC%25%5cD2%25%5cB3%25%5cC7&gnmkdm=N121113'
    resp=req.post(url,data=data)
    resp.encoding='gbk'
    print(resp.text)

#主程序，设置学号密码并运行
if __name__=='__main__':
    xh='xxx'
    psd='xxx'
    lt=getHduCookie()
    tmpurl=simLogin(lt)
    if tmpurl[0:4]=="http":
        print("登录成功，可跳转网址"+tmpurl)
    else:
        print("登录失败")
    #req=jxglPage(tmpurl)
    #classList(req)