from flask import Flask, render_template, Response, request
import cv2

app = Flask(__name__)

video_frame = None

@app.route('/')
def index():
    return render_template('index_v1.html')

def gen_frames():
    while True:
        if video_frame is not None:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + video_frame + b'\r\n')

@app.route('/video_feed', methods=['POST', 'GET'])
def video_feed():
    if request.method == 'POST':
        global rec_frame
        rec_frame = request.data
        return "Success"
    else:
        return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
    
@app.route('/requests', methods=['POST', 'GET'])
def tasks():
    global switch, camera
    if request.method == 'POST':
        if request.form.get('stop') == 'Stop/Start':
            if switch == 1:
                switch = 0
                camera.release()
                cv2.destroyAllWindows()    
            else:
                camera = cv2.VideoCapture(0)
                switch = 1

        return render_template('index_v1.html')  # Return a response for the 'POST' method

    elif request.method == 'GET':
        return render_template('index_v1.html')  # Return a response for the 'GET' method


if __name__ == '__main__':
    app.run(host='192.168.59.5', port=5000, debug=True, ssl_context='adhoc')
