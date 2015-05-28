from flask import Flask, request, session, g, redirect, url_for, \
	abort, render_template, flash, make_response
from os import environ

DEBUG = environ['DEBUG']
SECRET_KEY=environ['secret']

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def home():
	session['page']="home"
	return render_template('index.html')

if __name__=='__main__':
	port = int(environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)