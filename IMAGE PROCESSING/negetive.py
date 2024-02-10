import cv2 

img=cv2.imread('apple.jpg',1) 
height,width,channel=img.shape 

for i in range(height): 
 for j in range(width): 
  for k in range(channel): 
   img[i][j][k]=255-img[i][j][k]
cv2.imshow('neg', img) 
cv2.waitKey(0) 
