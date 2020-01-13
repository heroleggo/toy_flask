from flask import Flask, render_template, request, session
from scripts import query


app = Flask(__name__)
app.secret_key = 'this is secret key'


@app.route('/')
def main():
  return render_template('main.html')


@app.route('/info')
def info():
  return render_template('info.html')

@app.route('/programs')
def programs():
  return render_template('programs.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
  if request.method == 'POST':
    res = query.signup(request.form)
    print (res)
    return render_template('main.html')
  else:
    return render_template('signup.html')


@app.route('/signin', methods=['POST','GET'])
def signin():
  if request.method == 'POST':
    res = query.signin(request.form)
    print (res)
    if res == "success":
      session['logged_in'] = True
    else:
      session['logged_in'] = False
    return render_template('main.html')
  else:
    return render_template('signin.html')


@app.route('/signout')
def signout():
  session['logged_in'] = False
  return render_template('main.html')


if __name__ == '__main__':
  app.run(debug=True)
