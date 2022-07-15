from flask import Blueprint, render_template, request, flash, jsonify, redirect, current_app,url_for
from flask_login import login_required, current_user
from .models import Note,User
from .forms import editEmail,editNickname
from . import db
import json
import re

views = Blueprint('views', __name__)

@views.route('/favicon.ico')
def get_fav():
    return current_app.send_static_file('img/favicon.ico')


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id,nickname=current_user.nickname)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
            return redirect('/')

    notes=db.session.query(Note).order_by(Note.date.desc()).all()

    return render_template("home.html", user=current_user,notes=notes)


@views.route('/profile/<user_id>',methods=['GET', 'POST'])
@login_required
def profile(user_id):
    if request.method=='POST':
        return render_template("edit.html",user=current_user)
    accessingUser=User.query.get(user_id)
    return render_template("profile.html",user=current_user,accessingUser=accessingUser)


@views.route('/edit',methods=['GET', 'POST'])
@login_required
def edit():
    user=current_user
    edit_email=editEmail()
    edit_nickname=editNickname()
    if request.method == 'POST':
        if edit_email.submit1.data and edit_email.validate():
            email = edit_email.email.data
            if email==user.email:
                flash('The new email is same as before.', category='error')
            elif User.query.filter_by(email=email).first():
                flash('Email already exists.', category='error')
            elif not re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$',email):
                flash('Email must be valid.', category='error')
            else:
                User.query.filter(User.id == user.id).update({'email': email})
                db.session.commit()
            flash('%s, you have just submitted your new email address.' % email)
            return redirect(url_for('views.profile',user_id=user.id))

        if edit_nickname.submit2.data and edit_nickname.validate():
            nickname = edit_nickname.nickname.data
            if nickname==user.nickname:
                flash('The new email is same as before.', category='error')
            elif User.query.filter_by(nickname=nickname).first():
                flash('Email already exists.', category='error')
            elif len(nickname) < 2:
                flash('Nickname must be greater than 1 character.', category='error')
            else:
                User.query.filter(User.id == user.id).update({'nickname':nickname})
                db.session.commit()
                Note.query.filter(Note.user_id == user.id).update({'nickname':nickname})
                db.session.commit()
            flash('%s, you have just submitted your new nickname.' % nickname)
            return redirect(url_for('views.profile',user_id=user.id))
    return render_template("edit.html",user=current_user,edit_email=edit_email,edit_nickname=edit_nickname)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

