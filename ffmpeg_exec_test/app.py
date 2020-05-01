import cv2
import time
import ffmpeg_streaming
from ffmpeg_streaming import Formats, Bitrate, Representation, Size

from flask import render_template, Flask, send_from_directory, abort, json, \
   Response  # sudo python3 -m pip install flask

app = Flask('__name__')

@app.route('/')
def index():
   """Video streaming home page."""
   return render_template('index.html')

def gen():
   """Video streaming generator function."""
   x = 0
   while x < 7:
      cap = cv2.VideoCapture('video_fragments/hls_outputs_480p_000' + str(x) + '.ts')
      x = x + 1

      # Read until video is completed
      while (cap.isOpened()):
         # Capture frame-by-frame
         ret, img = cap.read()
         if ret == True:
            img = cv2.resize(img, (0,0), fx=1.4, fy=1.1)
            frame = cv2.imencode('.jpg', img)[1].tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            time.sleep(0.1)
         else:
            break

@app.route('/video_feed')
def video_feed():
   """Video streaming route. Put this in the src attribute of an img tag."""
   return Response(gen(),
                   mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
   app.run(host = "0.0.0.0", port = '5000')
