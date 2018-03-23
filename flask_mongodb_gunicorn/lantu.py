from flask import Blueprint,render_template,abort,session,request
from jinja2 import TemplateNotFound
from pymongo import MongoClient
import json

client=MongoClient()
db=client.test_database
posts=db.posts

simple_page=Blueprint('simple_page',__name__,template_folder='templates')

@simple_page.route("/main")
def main():
    if "username" in session:
        data={}
        data['username']=session['username']
        data['info']=[post for post in posts.find()]
        return render_template("main.html",data=data)
    else:
        return render_template('login.html')

@simple_page.route("/main/add",methods=['POST'])
def add():
    post={
        "name":request.form['name'],
        "email":request.form['email'],
        "phone":request.form['tel'],
        "more":request.form['more']
    }
    if posts.insert_one(post).inserted_id!="":
        return json.dumps({"state":"1000","result":"success"})
    else:
        return json.dumps({"state":"1004","result":"insert error"})

@simple_page.route("/main/dele",methods=['POST'])
def dele():
    result=posts.delete_one({"name":request.form['name']})
    if result.deleted_count>0:
        return json.dumps({"state":"1000","result":request.form['name']})
    else:
        return json.dumps({"state":"1005","result":"delete error"})

@simple_page.route("/main/edit",methods=['POST'])
def edit():
    result=posts.update_one({"name":request.form['org_name']},{"$set":{
        "name":request.form['ch_name'],
        "email":request.form['ch_email'],
        "phone":request.form['ch_phone'],
        "more":request.form['ch_more']
    }})
    if result.matched_count!=0:
        return json.dumps({"state":"1000","result":request.form['ch_name']})
    else:
        return json.dumps({"state":"1006","result":"edit error"})
    #return json.dumps({"state":"1000","result":result.matched_count})