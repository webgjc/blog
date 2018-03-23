from lantu import simple_page
from flask import Flask,render_template,request,session,redirect,url_for
import json
import hashlib

app=Flask(__name__)
app.secret_key='gjc'

app.register_blueprint(simple_page)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route("/login")
def login():
    if "username" not in session:
        return render_template('login.html')
    else:
        return redirect(url_for('simple_page.main'))

@app.route("/login/loginYz",methods=['POST'])
def loginyz():
    psd=hashlib.sha256()
    psd.update('root'.encode('utf-8'))
    if request.form['username']!='root':
        res={
            "state":"1001",
            "result":"username error"
        }
        return json.dumps(res)
    elif psd.hexdigest()!=request.form['password']:
        res={
            "state":"1002",
            "result":"password error"
        }
        return json.dumps(res)
    else:
        session['username'] = request.form['username']
        res={
            "state":"1000",
            "result":"success",
            "linkTo":"/main"
        }
        return json.dumps(res) 

@app.route("/loginout")
def loginout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__=='__main__':
    app.run("0.0.0.0",debug=True)