from flask import Flask, render_template, request, session
app = Flask(__name__)
app.secret_key = 'any random string'

@app.route("/")
def hello():
    return render_template('capture.html', name='name')

@app.route("/register")
def register():
    return render_template('register.html', name='name')

@app.route("/start_register", methods=["POST"])
def start_register(uid):
    uid = request.form['uid']
    # pwd = request.form['pwd']
    session['uid'] = uid
    return ""

@app.route("/register_face", methods=["POST"])
def register_face():
    uid = session['uid']
    with open("rimg%s.jpg" % uid, "wb") as f:
        data = request.get_data(cache=False)
        f.write(data)
    return ""

@app.route("/start_auth/<uid>")
def start_auth(uid):
    session['uid'] = uid
    return ""

@app.route("/upload", methods=["POST"])
def upload():
    uid = session['uid']
    with open("img%s.jpg" % uid, "wb") as f:
        data = request.get_data(cache=False)
        f.write(data)
    return "abc"
