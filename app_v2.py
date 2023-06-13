from flask import Flask, render_template, request
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_v2.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save('uploads/' + file.filename)
    return 'Upload successful!'

if __name__ == '__main__':
    app.run(host='192.168.59.5', port=5000, debug=True, ssl_context='adhoc')