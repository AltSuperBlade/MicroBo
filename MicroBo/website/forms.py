from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class editEmail(FlaskForm):
    old_email="123"
    email = StringField('Email Address', validators=[DataRequired(), Length(1,254)])
    submit1 = SubmitField('Edit Your Email')

class editNickname(FlaskForm):
    nickname = StringField('nickname', validators=[DataRequired(), Length(1,20)])
    submit2 = SubmitField('Edit your nickname')

class changePassword(FlaskForm):
    password1 = PasswordField('New password',validators=[DataRequired(),Length(8,128)])
    password2 = PasswordField('Confirm new password',validators=[DataRequired(),Length(8,128)])    
    submit3 = SubmitField('Confirm')