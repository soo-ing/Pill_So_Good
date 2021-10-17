#openSW
import requests, os, time, playsound
from gtts import gTTS
import speech_recognition as sr
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
pir=7
GPIO.setup(pir, GPIO.IN, GPIO.PUD_UP)

def speak(text):
    tts = gTTS(text='해당 알약은 '+text+' 입니다.', lang='ko')
    filename='voice1.mp3'
    tts.save(filename)
    return filename

while True:
    if GPIO.input(pir)==GPIO.LOW:
        time.sleep(2)
        os.system("raspistill -o imagePILL.jpg -t 3000")
        files = open('/home/pi/project/imagePILL.jpg', 'rb')
        upload = {'file':files}
        res = requests.post('http://172.30.1.2:8000/image', files = upload)
        print(res.text)
        playsound.playsound(speak(res.text))
        time.sleep(3)
