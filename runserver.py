from flask import Flask, request, session, g, redirect, url_for, \
	abort, render_template, flash, make_response
from os import environ
from wtforms import Form, TextField, PasswordField, validators
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from datetime import datetime
from flask.ext.login import LoginManager, login_user, logout_user, UserMixin, current_user, login_required

DEBUG = environ['DEBUG']
SECRET_KEY=environ['secret']
mongo_hq_url=environ['mongo_hq_url']

app = Flask(__name__)
app.config.from_object(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

client = MongoClient(mongo_hq_url)
db = client.app37656652

@app.route('/')
def home():
	session['page']="home"
	return render_template('index.html')


@app.route('/login', methods=['GET','POST'])
def login():
	session['page']="login"
	form = LoginForm(request.form)
	if request.method == 'POST' and form.validate():
		in_db = db.CLUsers.find_one({'username':form.username.data})
		if in_db:
			user = User(in_db)
			if check_password_hash(user.get('password'),form.password.data):
				login_user(user,force=True)
				return(redirect(url_for('videos')))
			else:
				flash("Incorrect password.")
		else:
			flash("Username doesn't exist.")
	return render_template('login.html', form = form)

@app.route('/register', methods=['GET','POST'])
def register():
	session['page']="register"
	form = RegisterForm(request.form)
	if request.method == 'POST' and form.validate():
		new_username = form.username.data
		if db.CLUsers.find_one({'username': new_username}):
			flash("Username already in use.")
			return redirect(url_for('register'))
		else:
			new_user = {
				'username': form.username.data,
				'password': generate_password_hash(form.password.data),
				'email': form.email.data,
				'validated': False
			}
		db.CLUsers.insert(new_user)
		flash("Account created.  Please check your email to validate your account.")
		return redirect(url_for('login'))
	return render_template('register.html', form=form)

#now updates based on internal ID parameters
#probably secure
#untested
@app.route('/validate/<account>')
def validate(acount):
	user = db.CLUsers.update({'_Id':ObjectId(account)},{'validated': True}, upsert=False)
	flash("Account validated.  Please login.")
	return redirect(url_for('login'))

@app.route('/logout')
def logout():
	session['page']="logout"
	logout_user()
	flash("You have been successfully logged out.")
	return redirect(url_for('login'))

#DEPRECIATED
@app.route('/videos')
@login_required
def videos():
	session['page']="videos"
	videos = ['d6c25935786a6a99cd6fc91519b8d3bcb90bd789', '6849f65ce22dfade51a62d76fb958f4fc2341f4e']
	return render_template('videos.html', videos = videos)

#DEPRECIATED
@app.route('/watch/<id>')
@login_required
def watch(id):
	session['page']="watch"
	video = {'name': 'Name',
			'id': id,
			'desc': 'Here is the description of each video.'}
	return render_template('watch.html', video = video)

class User(dict, UserMixin):
	pass
	def get_id(self):
		return str(self.get('_id'))

class RegisterForm(Form):
	username = TextField('Username', [validators.Length(min=4,max=20)])
	password = PasswordField('Password', [validators.Length(min=5,max=20)])
	email = TextField('Email Address', [validators.Length(min=10,max=30)])

class LoginForm(Form):
	username = TextField('Username', [validators.Length(min=4, max=20)])
	password = PasswordField('Password', [validators.Length(min=5, max=25)])

@login_manager.user_loader
def load_user(userid):
	return User(db.CLUsers.find_one({'_id':ObjectId(userid)}))

@app.template_filter('currency')
def format_currency(value):
    return "${:,.2f}".format(value)

if __name__=='__main__':
	port = int(environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)