from ml import get_features, do_faces_match, is_alive

from flask import Flask, render_template, request, session, jsonify
app = Flask(__name__)
app.secret_key = 'any random string'

@app.route("/")
def hello():
    return render_template('capture.html', name='name')

@app.route("/register")
def register():
    return render_template('register.html')

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
    session['frame_count'] = 0
    return ""

@app.route("/upload", methods=["POST"])
def upload():
    uid = session['uid']
    impath = "img%s.jpg" % uid
    with open(impath, "wb") as f:
        data = request.get_data(cache=False)
        f.write(data)
    features = get_features(impath)
    actual_features = get_features("r" + impath)
    success = do_faces_match(actual_features, features)
    if not success:
        return jsonify({ 'status': False })
    session['frame_count'] = session['frame_count'] + 1
    if session['frame_count'] == 1:
        return jsonify({ 'status': True, 'done': False })
    success = is_alive(session['features'], features)
    if not success:
        return jsonify({ 'status': False })
    session['features'] = features
    if session['frame_count'] == 5:
        return jsonify({ 'status': True, 'done': True })
    return jsonify({ 'status': True, 'done': False })
