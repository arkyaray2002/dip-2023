import cv2
import numpy as np

img = cv2.imread('apple.jpg')
red = img.copy()
red[:,:,2]=0
green = img.copy()
green[:,:,1]=0
blue = img.copy()
blue[:,:,0]=0

cv2.imshow('red eleminated', red)
cv2.imshow('green eleminated', green)
cv2.imshow('blue eleminated', blue)

cv2.waitKey(0)