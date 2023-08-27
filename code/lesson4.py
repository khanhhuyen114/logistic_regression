import cv2
import numpy as np

img = cv2.imread('Sources/testpic.png', 1)
# print(img.shape)
# crp_img = img[100:400, 150:500]
# cv2.imshow('Test pic', img)
# cv2.imshow('Cropped pic', crp_img)
# cv2.waitKey(0)

# Divide into small patches
heigh = img.shape[1]
width = img.shape[0]
img_copy = img.copy()
x, y  = 0, 0
M = 76
N = 104
for y in range(0,heigh, M):
    for x in range(0, width, N):
        if (heigh - y) < M or (width - x) < N:
            break
        y1 = y + M
        x1 = x + N
        if x1 >=  width:
            x1 -= 1
        if y1 >= heigh:
            y1 -= 1
        tile = img_copy[x:x+N, y:y + M]
        cv2.imwrite('save patches.jpg', tile)
        cv2.rectangle(img, (x,y), (x1,y1), (0, 255, 0), 1)
cv2.imshow('Patches Image', img)
cv2.imwrite('Patched.jpg', img)
cv2.waitKey(0)
cv2.destroyWindow()





