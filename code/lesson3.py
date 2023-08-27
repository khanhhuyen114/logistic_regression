import cv2
import numpy as np

img = cv2.imread('Sources/lesson3 pic.png', 1)
h, w, c = img.shape
## Resize by definiting heigh and width
# h_down = 200
# w_down = 300
# size_down = (w_down, h_down)
# img_down = cv2.resize(img, size_down, interpolation = cv2.INTER_LINEAR)

# h_up = 400
# w_up = 600
# size_up = (w_up, h_up)
# img_up = cv2.resize(img, size_up, interpolation = cv2.INTER_LINEAR)

# cv2.imshow('Downsize Image', img_down)
# cv2.imshow('Upsize Image', img_up)

## Resize by Scaling factor
scale_up_x = 1.2
scale_up_y = 1.2
scale_down = 0.6

img_scaleup = cv2.resize(img,None, fx = scale_up_x, fy = scale_up_y, interpolation = cv2.INTER_LINEAR)
img_scaledown = cv2.resize(img, None,fx = scale_down, fy = scale_down, interpolation= cv2.INTER_LINEAR)

## Resize by different interpolation methods
res_inter_area = cv2.resize(img,None, fx = scale_up_x, fy = scale_up_y, interpolation = cv2.INTER_AREA)
res_inter_nearest = cv2.resize(img,None, fx = scale_up_x, fy = scale_up_y, interpolation = cv2.INTER_NEAREST)



# cv2.imshow('Original Image', img)
# cv2.imshow('Downsize Image', img_scaledown)
# cv2.imshow('Upsize Image', img_scaleup)

cv2.imshow('inter_area_img', res_inter_area)
cv2.imshow('inter_nearest_img', res_inter_nearest)

cv2.waitKey(0)
cv2.destroyAllWindows()