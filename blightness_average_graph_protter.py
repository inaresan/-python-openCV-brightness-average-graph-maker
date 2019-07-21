# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""
import cv2
import numpy as np
from matplotlib.pyplot import imshow
image_path="C:/Users/B1703/data/"
cap = cv2.VideoCapture(image_path+"test2.mp4")
l = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
count=0;
graph=np.zeros(shape=l, dtype=np.uint8)
imgr=np.zeros(shape=(256,l,3),dtype=np.uint8)

for k in range(l):
    # フレームを取得
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    bls=0
    h,w=gray.shape
    for i in range(h):
        for j in range(w):
            bls=bls+gray[i,j]
    print(bls/h/w)
    graph[k]=bls/h/w
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
imgr[:,:,:]=[255,255,255]
for i in range(l):
    imgr[255-graph[i]:255,i,:]=[0,0,255]
imshow(imgr)

