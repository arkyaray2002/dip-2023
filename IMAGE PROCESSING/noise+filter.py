import cv2
import numpy as np

def add_gaussian(img,mean=0,sigma=25):
    row,col=img.shape
    gauss=np.random.normal(mean,sigma,(row,col))
    noisy=np.clip(img+gauss,0,255)
    noisy=noisy.astype(np.uint8)
    return noisy

def mean_filter(image,kernal):
    height,width=image.shape[:2]

    result=np.zeros_like(image,dtype=np.float32)
    for i in range(kernal//2,height-kernal//2):
        for j in range(kernal//2,width-kernal//2):
            result[i,j]=np.mean(image[i-kernal//2:i+kernal//2+1,j-kernal//2:j+kernal//2+1])

    result=result.astype(np.uint8)
    return result


org_img = cv2.imread("apple.jpg",0)

noisy_img = add_gaussian(org_img)

filtered_image = mean_filter(noisy_img,3)

cv2.imshow("Noisy Image",noisy_img)
cv2.imshow("Filtered Image",filtered_image)
cv2.waitKey(0)