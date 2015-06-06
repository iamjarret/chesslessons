from flask import Flask, request, session, g, redirect, url_for, \
	abort, render_template, flash, make_response
from os import environ
from wtforms import Form, TextField, PasswordField, validators

DEBUG = environ['DEBUG']
SECRET_KEY=environ['secret']

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def home():
	session['page']="home"
	return render_template('index.html')


@app.route('/login', methods=['GET','POST'])
def login():
	session['page']="login"
	form = LoginForm(request.form)
	if request.method == 'POST' and form.validate():
		if form.username.data == 'Test' and form.password.data == 'TestTest':
			return(redirect(url_for('videos')))
	return render_template('login.html', form = form)

@app.route('/videos')
def videos():
	session['page']="videos"
	videos = ['d6c25935786a6a99cd6fc91519b8d3bcb90bd789', '6849f65ce22dfade51a62d76fb958f4fc2341f4e']
	return render_template('videos.html', videos = videos)

@app.route('/watch/<id>')
def watch(id):
	session['page']="watch"
	video = {'name': 'Name',
			'id': id,
			'desc': 'Here is the description of each video.'}
	return render_template('watch.html', video = video)

class LoginForm(Form):
	username = TextField('Username', [validators.Length(min=2, max=25)])
	password = TextField('Password', [validators.Length(min=2, max=25)])

if __name__=='__main__':
	port = int(environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)