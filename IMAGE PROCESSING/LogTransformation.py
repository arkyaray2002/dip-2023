import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
img=cv2.imread('Taj.jpg',0) 

histogram=cv2.calcHist([img],[0],None,[256],[0,255]) 
plt.plot(histogram) 
height,width=img.shape[:2] 

def evaluatePixelStatic(pixel): 
  return np.log10(pixel+1) 
def evaluatePixelDynamic(pixel): 
  return (255/np.log10(1+255))*np.log10(pixel+1) 
for i in range(height): 
  for j in range(width): 
    img[i][j]=evaluatePixelDynamic(img[i][j]) 

cv2.imshow('Log',img) 
histogram=cv2.calcHist([img],[0],None,[256],[0,255]) 
plt.plot(histogram) 
plt.show() 
cv2.waitKey(0) 
