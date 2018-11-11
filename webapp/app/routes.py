from flask import render_template, request

from app import app
# from app import mongo

@app.route('/')
def indexPage():
    user = request.cookies.get('username')
    return render_template('index.html', user=user)

@app.route('/rent')
def rentPage():
    user = request.cookies.get('username')
    return render_template('rent.html', user=user)

@app.route('/host')
def hostPage():
    user = request.cookies.get('username')
    return render_template('host.html', user=user)

@app.route('/login')
def loginPage():
    user = request.cookies.get('username')
    return render_template('login.html', user=user)

@app.route('/signup')
def signupPage():
    user = request.cookies.get('username')
    return render_template('signup.html', user=user)

@app.route('/editor')
def editorPage():
    user = request.cookies.get('username')
    return render_template('editor.html', user=user)

@app.route('/profile')
def profilePage():
    user = request.cookies.get('username')
    return render_template('profile.html', user=user)

@app.route('/api/send_code', methods=['POST'])
def sendCode():
    body = request.get_json()
    socketio.emit('code_send', body['code'])
    return 'Code sent'
