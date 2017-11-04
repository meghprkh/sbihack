from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('capture.html', name='name')

@app.route("/upload", methods=["POST"])
def upload():
    with open("img.jpg", "wb") as f:
        data = request.get_data(cache=False)
        f.write(data)
    return "abc"
