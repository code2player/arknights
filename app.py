from utils.Database import QueryWithConnect
from flask import Flask, jsonify, g, request, abort, make_response, send_from_directory, render_template, session, redirect, url_for, flash
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from utils.Database import MySQL
from utils.Token import Token



import re
from datetime import datetime
import json
import os
import base64

# 服务端的代码需要开启db以及登录验证中的ip

# 连接数据库
db = MySQL()
db.db.ping(reconnect=True)


app = Flask(__name__, static_url_path='')
app.secret_key = "affedasafafqwe"
auth_user = HTTPBasicAuth()  # 用户名和密码验证
auth_token = HTTPTokenAuth()  # token验证
CORS(app, supports_credentials=True)

# app的配置选项
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"

user_now_name =""

# 用户名和密码验证
@auth_user.verify_password
def verify_password(username, password):
    # 验证用户id与密码是否匹配
    print(username, password)
    label = db.hasUser(username, password)

    # 如果用户id与密码对应不上，返回False
    if not label:
        return False
    g.ID = username
    return True


# token验证
@auth_token.verify_token
def verify_token(token):
    token = re.sub(r'^"|"$', '', token)
    label = Token.verify_auth_token(token)
    g.user_id = label['user_id']
    #g.user_name = db.getUser(g.user_id)
    return label


# 主页
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('search_context')
        res = db.searchOperator(name)
        if res:
            return redirect(url_for('operator_arts',operator_name=name))  # 重定向
    return render_template('index.html', ID=session.get('username'))


# 注册用户
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        ID = request.form.get('ID')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        email = request.form.get('email')
        phone = request.form.get('phone')
        if(password1==password2):
            res = db.addUser(ID, password1, email, phone)
            if res:

                #flash('添加成功')  # 显示错误提示
                return redirect(url_for('login'))  # 重定向回主页
            else:
                flash('添加失败，用户已存在')  # 显示错误提示
                return redirect(url_for('register'))  # 重定向回主页
        else:
            flash('两次输入的密码不一样')  # 显示错误提示
            return redirect(url_for('register'))  # 重定向回主页
    else:
        return render_template('register.html')

# 登录验证
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        ID = request.form.get('ID')
        password = request.form.get('password')
        label = db.hasUser(ID, password)
        if not label:
            flash('用户名与密码不匹配')  # 显示错误提示
            return redirect(url_for('login'))  # 重定向
        session['username'] = ID
        return redirect(url_for('home'))  # 重定向
        #return render_template('index.html', ID=g.ID)
    else:
        return render_template('login.html')


# 干员美术资源
@app.route('/operator/<operator_name>/arts', methods=['GET', 'POST'])
def operator_arts(operator_name):
    if request.method == 'POST':
        name = request.form.get('search_context')
        res = db.searchOperator(name)
        if res:
            return redirect(url_for('operator_arts',operator_name=name))  # 重定向
    #返回一个list
    skins = db.getSkins(operator_name)
    voices = db.getVoices(operator_name)
    return render_template('arts.html', skins=skins, voices=voices, ID=session.get('username'))

# 干员档案信息
@app.route('/operator/<operator_name>/details', methods=['GET', 'POST'])
def operator_text(operator_name):
    if request.method == 'POST':
        name = request.form.get('search_context')
        res = db.searchOperator(name)
        if res:
            return redirect(url_for('operator_arts',operator_name=name))  # 重定向
    details = db.getDetails(operator_name)
    base_info = db.getBaseinfo(operator_name)
    return render_template('details.html', details=details, base_info=base_info, ID=session.get('username'))

# 干员战斗相关
@app.route('/operator/<operator_name>/fight', methods=['GET', 'POST'])
def operator_fight(operator_name):
    if request.method == 'POST':
        name = request.form.get('search_context')
        res = db.searchOperator(name)
        if res:
            return redirect(url_for('operator_arts',operator_name=name))  # 重定向
    attribute = db.getAttribute(operator_name)
    skills = db.getSkills(operator_name)
    return render_template('fight.html', attribute=attribute, skills=skills, ID=session.get('username'))






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5051, debug=True)