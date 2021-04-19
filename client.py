from __future__ import print_function
from flask import Flask
import json
import requests
import cv2

# Initialize the Flask application
app = Flask(__name__)

addr = 'http://server.pythonanywhere.com'
test_url = addr + '/api/test'
token = 'f25e6a55920de88a0f9e6ae923850bda3238f4bc'

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'Authorization': 'Token {token}'.format(token=token), 'content-type': content_type}

img = cv2.imread('wallpaper.jpg')
# encode image as jpeg
_, img_encoded = cv2.imencode('.jpg', img)
# send http request with image and receive response
response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
print(json.loads(response.content))


# expected output: {u'message': u'image received. size=124x124'}