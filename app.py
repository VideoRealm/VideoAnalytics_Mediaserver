import cv2
import time
import acapture
import ffmpeg
import pygame
import pygame.camera
from pygame.locals import *
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

   #image = ffmpeg.get_image()
   """Video streaming generator function."""
   #while True:

   #Failed option 1
   cap = ffmpeg.input('video_fragments/hls_outputs_480p_0000.ts')
   cap = ffmpeg.filter(cap, 'scale', 500, 500)
   ffmpeg.run(cap)

   #Failed option 2
   cap = acapture.open('video_fragments/hls_outputs_480p_0000.ts')

   while True:
      # Capture frame-by-frame
      check, frame = cap.read()
      if check == True:
         img = cv2.resize(img, (0,0), fx=1.5, fy=1.5)
         frame = cv2.imencode('.jpg', img)[1].tobytes()
         yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
         time.sleep(0.1)
      else:
         break

   #Failed option 3
   pygame.init()
   video = pygame.movie.Movie('video_fragments/hls_outputs_480p_0000.ts')
   video.play()



@app.route('/video_feed')
def video_feed():
   """Video streaming route. Put this in the src attribute of an img tag."""
   return Response(gen(),
                   mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
   app.run(host = "0.0.0.0", port = '5038')
