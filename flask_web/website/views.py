from flask import Blueprint, render_template, request, flash, jsonify, redirect, current_app,url_for,make_response,render_template_string
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from datetime import timedelta
from .models import Note,User
from .forms import editEmail,editNickname,changePassword
from . import db
import json
import cv2
import re
import os


views = Blueprint('views', __name__)


@views.route('/favicon.ico')
def get_fav():
    # 网页图标
    return current_app.send_static_file('img/favicon.ico')


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    # home广场
    if request.method == 'POST':
        # 新增留言
        note = request.form.get('note')

        if len(note) < 1:
            # 判断长度
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
            return redirect('/')

    notes=db.session.query(Note).order_by(Note.date.desc()).all()
    users=db.session.query(User).order_by(User.id.desc()).all()

    return render_template("home.html", user=current_user,notes=notes,users=users)


@views.route('/profile/<user_id>',methods=['GET', 'POST'])
@login_required
def profile(user_id):
    # 个人资料页面
    accessingUser=User.query.get(user_id) # 根据请求url获得被访问用户id
    return render_template("profile.html",user=current_user,accessingUser=accessingUser)


@views.route('/edit',methods=['GET', 'POST'])
@login_required
def edit():
    # 编辑邮箱和昵称页面
    user=current_user
    edit_email=editEmail()
    edit_nickname=editNickname()
    if request.method == 'POST':
        if edit_email.submit1.data and edit_email.validate():
            # 判断提交的是否为邮箱表单
            email = edit_email.email.data
            if email==user.email: # 防止修改后和原先相同
                flash('The new email is same as before.', category='error')
            elif User.query.filter_by(email=email).first(): # 防止与其他用户重复
                flash('Email already exists.', category='error')
            elif not re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$',email): # 检查邮箱格式
                flash('Email must be valid.', category='error')
            else:
                User.query.filter(User.id == user.id).update({'email': email})
                db.session.commit()
                flash('%s, you have just submitted your new email address.' % email,category='success')
            return redirect(url_for('views.profile',user_id=user.id))

        if edit_nickname.submit2.data and edit_nickname.validate():
            # 判断提交的是否为昵称表单
            nickname = edit_nickname.nickname.data
            if nickname==user.nickname: # 防止与原先重复
                flash('The new email is same as before.', category='error')
            elif User.query.filter_by(nickname=nickname).first(): # 防止与其他用户重复
                flash('Email already exists.', category='error')
            elif len(nickname) < 2: # 保证昵称长度
                flash('Nickname must be greater than 1 character.', category='error')
            else:
                User.query.filter(User.id == user.id).update({'nickname':nickname})
                db.session.commit()
                flash('%s, you have just submitted your new nickname.' % nickname,category='success')
            return redirect(url_for('views.profile',user_id=user.id))
    return render_template("edit.html",user=current_user,edit_email=edit_email,edit_nickname=edit_nickname)


@views.route('/change-password',methods=['GET', 'POST'])
@login_required
def ChangePassword():
    # 修改密码页面
    change_password=changePassword()
    if request.method == 'POST':
        password1=change_password.password1.data
        password2=change_password.password2.data
        if password1 != password2:
            # 判断两次密码是否一致
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 8:
            # 密码长度限制
            flash('Password must be at least 8 characters.', category='error')
        elif re.search(r'[_]|[\W]', password1)==None:
            # 密码强度限制
            flash('Password must have special characters.', category='error')
        else:
            User.query.filter(User.id == current_user.id).update({'password':generate_password_hash(password1, method='sha256')})
            db.session.commit()
            flash('Password changed!',category='success')
            return redirect(url_for('views.profile',user_id=current_user.id))
    return render_template("change_password.html",user=current_user,change_password=change_password)


#设置允许的文件格式
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
 
# 设置静态文件缓存过期时间
views.send_file_max_age_default = timedelta(seconds=1)
 
@views.route('/upload', methods=['POST', 'GET'])
@login_required
def upload():
    # 上传更新头像页面
    if request.method == 'POST':

        user=current_user
        f = request.files['file']
        if not (f and allowed_file(f.filename)):
            flash('Please check your format, we only accept png、PNG、jpg、JPG、bmp', category='error')
        else:
            basepath = os.path.dirname(__file__)  # 当前文件所在路径

            upload_path = os.path.join(basepath, 'static/images',secure_filename(f.filename))  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
            f.save(upload_path)

            User.query.filter(User.id == user.id).update({'portraitLink': secure_filename(f.filename)})
            db.session.commit()
            flash('Congratuation, you have just altered your portrait.',category="success")
            return redirect(url_for('views.profile',user_id=user.id))
 
    return render_template('upload.html',user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    # 删除留言功能
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


@views.route("/index/")
def ssti():
    # try to access 'http://127.0.0.1:5000/index/?content=<script>alert(/xss/)</script>'
    content = request.args.get("content")
    return render_template_string(content)