import cv2, dlib, sys
import numpy as np

cap = cv2.VideoCapture('video.mp4')

while True:
    ret, img = cap.read()
    if not ret:
        break

    cv2.imshow('img', img)
    cv2.waitKey(1)