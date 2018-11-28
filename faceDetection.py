# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 14:43:11 2018

@author: Abhishek
"""
import cv2

def detect(filename):
    face_cascade =cv2.CascadeClassifier('C:\\Users\\Abhishek\\Anaconda3\\pkgs\\libopencv-3.4.1-h875b8b8_3\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 2.1, 5)
    print(faces)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("sample",img)
    cv2.waitKey(0)

filename = 'C:\\Users\\Abhishek\\DataSet\\161500023.png'
detect(filename)
