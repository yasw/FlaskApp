from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,BooleanField,SubmitField,PasswordField
from wtforms.validators import EqualTo,DataRequired,Length,Email,ValidationError
from flaskblog.models import User
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed
class RegistrationForm(FlaskForm):
	username=StringField('Username',
		validators=[DataRequired(),Length(min=2,max=20)])
	email=StringField('Email',
		validators=[DataRequired(),Email()])
	password= PasswordField('Password',
		validators=[DataRequired()])
	confirm_password= PasswordField('Confirm Password',
		validators=[DataRequired(),EqualTo('password')])
	submit=SubmitField('Sign Up')

	def validate_username(self,username):
		user=User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('That username is taken')	
	def validate_email(self,email):
		user=User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('That email is taken')	

class LoginForm(FlaskForm):
	email=StringField('Email',
		validators=[DataRequired(),Email()])
	password= PasswordField('Password',
		validators=[DataRequired()])
	remember=BooleanField('Remeber Me')
	submit=SubmitField('Login')	

class UpdateAccountForm(FlaskForm):
	username=StringField('Username',
		validators=[DataRequired(),Length(min=2,max=20)])
	email=StringField('Email',
		validators=[DataRequired(),Email()])
	picture = FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])
	submit=SubmitField('Update')

	def validate_username(self,username):
		if username.data!=current_user.username:
			user=User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('That username is taken')	
	def validate_email(self,email):
		if email.data!=current_user.email:
			user=User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('That email is taken')

class PostForm(FlaskForm):
	title=StringField('Title',validators=[DataRequired()])
	content=TextAreaField('Content',validators=[DataRequired()])
	submit=SubmitField('Post')		
