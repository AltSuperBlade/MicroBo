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
    user_id = User.query.filter_by(nickname=nickname).first().id
    accessingUser=User.query.get(user_id)
    return render_template("profile.html",user=current_user,accessingUser=accessingUser)
# @views.route('/profile', methods=['GET'])
# @login_required
# def profile():
#     return render_template("profile.html",user=current_user,locationid=current_user.id)

# @views.route('/profile', methods=['POST'])
# @login_required
# def accessprofile():
#     return render_template("profile.html",user=current_user,locationid=request.form['noteUserId'])

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

# @views.route('/go-profile', methods=['GET','POST'])
# def go_profile():
#     # note = json.loads(request.data)
#     # noteId = note['noteId']
#     # note = Note.query.get(noteId)
#     return render_template("profile.html",user=current_user,locationid=note.user_id)

#    return jsonify({})
