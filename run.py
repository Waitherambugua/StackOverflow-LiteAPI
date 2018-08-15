from flask import Flask, render_template, url_for
from model.py import SignUpForm, LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "17a0ff2d80017591818a5481f7e35e8b"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/Login')
def Login():
	form = LoginForm()
	return render_template('Login.html')

@app.route('/SignUp')
def SignUp():
	form = SignUpForm()
	return render_template('SignUp.html', title="SignUp", form=form)

@app.route('/Forum')
def Forum():
	return render_template('Forum.html')

@app.route('/UserAccount')
def UserAccount():
	return render_template('UserAccount.html')

@app.route('/Questions')
def Questions():
	return render_template('Questions.html')

@app.route('/ForumAnswers')
def ForumAnswers():
	return render_template('ForumAnswers.html')




if __name__ =="__main__":
	app.run(debug=True)