#!/usr/bin/env python
import RPi.GPIO as GPIO
from flask import Flask, render_template, Response

# emulated camera
#from camera import Camera

# Raspberry Pi camera module (requires picamera package)
from camera_pi import Camera

app = Flask(__name__)

@app.route('/video/<action>')
def video_onoff(action):
    video_on = True
    print(action)
    if action == 'on':
        video_on = True
        GPIO.output(13, GPIO.HIGH)
    elif action == 'off':
        video_on = False
        GPIO.output(13, GPIO.LOW)
    else:
        pass

    templateData = {
        'video_on' : video_on
    }
    return render_template('index.html', **templateData )
@app.route('/led/<action>')
def led_onoff(action):
    if action== 'on':
        GPIO.output(11, GPIO.HIGH)
    elif action == 'off':
    	GPIO.output(11, GPIO.LOW)
    else:
        pass

    if GPIO.input(13) == GPIO.HIGH:
        video_on=True
    if GPIO.input(13) == GPIO.LOW:
        video_on = False

    templateData = {
        'video_on' : video_on
    }
    return render_template('index.html', **templateData )

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    app.run(host='0.0.0.0', debug=True, threaded=True)
