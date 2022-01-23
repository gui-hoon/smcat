from django.shortcuts import render
from django.views.decorators import gzip
from django.http import StreamingHttpResponse

import cv2
import threading

# Create your views here.    

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(1)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@gzip.gzip_page
def mycctv(request):

    return render(request, 'cctv/mycctv.html', {})

def mycam(request):
    try:
        _cam = VideoCamera()
        return StreamingHttpResponse(gen(_cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        print("video does not exist")
    
    # return render(_cam, 'cctv/mycam.html')