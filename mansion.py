from flask import Flask, render_template, url_for
from form import RegisterForm
from flask_fontawesome import FontAwesome

app = Flask(__name__)
fa = FontAwesome(app)
app.config['SECRET_KEY'] = 'thisissecretkey'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)

@app.route('/forgotpassword')
def forgotpassword():
    return render_template('forgotpassword.html')

if __name__ == '__main__':
    app.run(debug=True)
