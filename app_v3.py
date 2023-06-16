from flask import Flask, render_template, request
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_v3.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        file.save('uploads/' + file.filename)
        return 'Upload successful!'
    else:
        return 'No file received'

if __name__ == '__main__':
    app.run(host='192.168.59.5', port=5000, debug=True, ssl_context='adhoc')