from flask import Blueprint, render_template, request, flash, jsonify, redirect, current_app
from flask_login import login_required, current_user
from .models import Note
from .models import User
from . import db
import json

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


@views.route('/profile/<nickname>',methods=['GET', 'POST'])
@login_required
def profile(nickname):
    if request.method=='POST':
        return render_template("edit.html",user=current_user)
    user_id = User.query.filter_by(nickname=nickname).first().id
    accessingUser=User.query.get(user_id)
    return render_template("profile.html",user=current_user,accessingUser=accessingUser)


@views.route('/edit',methods=['GET', 'POST'])
@login_required
def edit():
    if request.method == 'POST':
        email = request.form.get('email')
        nickname = request.form.get('nickname')

        if user:
            flash('Email already exists.', category='error')
        elif not re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$',email):
            flash('Email must be valid.', category='error')
        elif len(nickname) < 2:
            flash('Nickname must be greater than 1 character.', category='error')
        else:
            # new_user = User(email=email, nickname=nickname, password=generate_password_hash(
            #     password1, method='sha256'))
            # db.session.add(new_user)
            # db.session.commit()
            # login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.profile/<nickname>'))
    return render_template("edit.html",user=current_user)


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

