import cv2
import urllib.request
import numpy as np
import imutils

url = "http://192.168.43.1:8080/shot.jpg"
while True:
    imgPath = urllib.request.urlopen(url)
    imgnp = np.array(bytearray(imgPath.read()),dtype=np.uint8)
    img = cv2.imdecode(imgnp,-1)
    img = imutils.resize(img,width=450)
    cv2.imshow("camearFeed",img)
    if ord('q') == cv2.waitKey(1):
        exit(0)
