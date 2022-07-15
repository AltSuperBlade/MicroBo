from wtforms.validators import Email
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class editEmail(FlaskForm):
    old_email="123"
    email = StringField('Email Address', validators=[DataRequired(), Length(1,254)])
    submit1 = SubmitField('Edit Your Email')

class editNickname(FlaskForm):
    nickname = StringField('nickname', validators=[DataRequired(), Length(1,20)])
    submit2 = SubmitField('Edit your nickname')