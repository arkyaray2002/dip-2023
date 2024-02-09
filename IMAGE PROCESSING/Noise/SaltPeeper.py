import cv2
import numpy as np

def add_salt_and_peeper(img , salt,peeper):
    noisy=np.copy(img)

    salt_pixel=np.random.rand(*img.shape)<salt
    noisy[salt_pixel]=255

    peeper_pixel=np.random.rand(*img.shape)<peeper
    noisy[peeper_pixel]=0
    return noisy

org_img=cv2.imread("apple.jpg",0)
salt=0.02
peeper=0.02
noisy_img=add_salt_and_peeper(org_img,salt,peeper)
cv2.imshow("Noisy Image",noisy_img)
cv2.waitKey(0)
