import cv2 
img=cv2.imread('Taj.jpg') 
height,width=img.shape[:2] 
for i in range(height): 
 for j in range(width): 
  img[i][j]=255-img[i][j] 
cv2.imshow('neg', img) 
cv2.waitKey(0) 
