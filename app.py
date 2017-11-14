from ml import get_features, get_features_np, do_faces_match, is_alive
import numpy as np
import cv2
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
    session['features'] = None
    session['uid'] = uid
    session['frame_count'] = 0
    session['alive_sum'] = 0
    return ""

@app.route("/upload", methods=["POST"])
def upload():
    uid = session['uid']
    impath = "img%s.jpg" % uid
    data = request.get_data(cache=False)
    imarr = np.asarray(bytearray(data), dtype=np.uint8)
    img = cv2.imdecode(imarr, cv2.IMREAD_UNCHANGED)
    features = get_features_np(img)
    actual_features = get_features("r" + impath)
    success = do_faces_match(actual_features, features)
    if not success:
        return jsonify({ 'status': False })
    session['frame_count'] = session['frame_count'] + 1
    if session['frame_count'] == 1 or not session['features']:
        session['features'] = features.tostring()
        return jsonify({ 'status': True, 'done': False })
    old_features = np.fromstring(session['features'], dtype=np.float)
    session['alive_sum'] = session['alive_sum'] + is_alive(old_features, features)
    session['features'] = features.tostring()
    if session['frame_count'] == 5:
        print(session['alive_sum'])
        if session['alive_sum'] > 0.4:
            return jsonify({ 'status': True, 'done': True })
        else:
            return jsonify({ 'status': False })
    return jsonify({ 'status': True, 'done': False })

app.run(host='0.0.0.0', port=8000)
