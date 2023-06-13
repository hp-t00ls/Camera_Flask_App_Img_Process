from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_v1.html')

if __name__ == '__main__':
    app.run(host='192.168.59.5', port=5000, debug=True, ssl_context='adhoc')
