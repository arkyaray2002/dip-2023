import cv2
image = cv2.imread('rose.jpg')
b = image.copy()
b[:,:,1]=0
b[:,:,2]=0
g = image.copy()
g[:,:,0]=0
g[:,:,2]=0
r = image.copy()
r[:,:,0]=0
r[:,:,1]=0
cv2.imshow('B_RGB',b)
cv2.imshow('G_RGB',g)
cv2.imshow('R_RGB',r)
cv2.waitKey(0)