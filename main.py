from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

def is_blank(str):
    if str == []:
        return True

@app.route("/signup", methods=['POST'])
def validation():
    username = request.form['username']
    password = request.form['password']
    password_conf = request.form['password_conf']
    email = request.form['email']

    username_error = ''
    password_error = ''
    password_conf_error = ''
    email_error = ''

    if is_blank(username):
        username_error = 'Not a valid username'
        username = ''
    else:
        if len(username) > 20 or len(username) < 3:
            username_error = 'Username out of range (3-20 characters)'
            username = ''

    if is_blank(password):
        password_error = 'Please enter a password'
        password = ''
    else:
        if len(password) > 20 or len(password) < 3:
            password_error = 'Password out of range (3-20 characters)'
            password = ''
    
    if password_conf != password:
        password_conf_error = 'Password Must match!'
        password_conf = ''

    if email:
        if email.count("@") < 1 or email.count("@") > 1:
            email_error = 'Please enter a valid email!'
        if email.count(".") < 1 or email.count(".") > 1:
            email_error = 'Please enter a valid email!'
        if " " in email:
            email_error = "Please enter a valid email!"
        if len(email) < 3 or len(email) > 20:
            email_error = "Email length out of range(3-20)"

    if not username_error and not password_error and not password_conf_error and not email_error:
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('user-signup.html',
                                username_error=username_error,
                                password_error=password_error,
                                password_conf_error=password_conf_error,
                                email_error=email_error,
                                username=username,
                                email=email)

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', user=username)                                
@app.route("/")
def index():
    return render_template('user-signup.html')

app.run()