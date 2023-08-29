import cv2
import numpy as np

# Use contour in Opencv
img = cv2.imread('Sources/pic6.png', 1)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY) #Thresh: binary image
thresh = thresh.astype(np.uint8)
contours, hierachy = cv2.findContours(image=thresh, mode = cv2.RETR_TREE, method = cv2.CHAIN_APPROX_NONE)
img_copy = img.copy()
cv2.drawContours(img_copy, contours, contourIdx= -1, color=(0,0,255), thickness= 3, lineType= cv2.LINE_AA)

# Use Single Channel: Red, Green, Blue
blue, green, red = cv2.split(img)
contours1, hierachy1 = cv2.findContours(blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
img_blue = img.copy()
cv2.drawContours(img_blue, contours1, contourIdx= -1, color = (0,255,0), thickness = 2, lineType= cv2.LINE_AA)
cv2.imshow('Blue Contour Image', img_blue)
cv2.waitKey(0)
cv2.imwrite('blue_channel.png', img_blue)

contours2, hierachy2 = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
img_red = img.copy()
cv2.drawContours(img_red, contours2, contourIdx= -1, color = (0,255,0), thickness = 2, lineType= cv2.LINE_AA)
cv2.imshow('red Contour Image', img_red)
cv2.waitKey(0)
cv2.imwrite('red_channel.png', img_red)

contours3, hierachy3 = cv2.findContours(green, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
img_green = img.copy()
cv2.drawContours(img_green, contours1, contourIdx= -1, color = (0,255,0), thickness = 2, lineType= cv2.LINE_AA)
cv2.imshow('Green Contour Image', img_green)
cv2.waitKey(0)
cv2.imwrite('Green_channel.png', img_green)
cv2.destroyAllWindows()
cv2.imshow('Binary image', thresh)
cv2.imwrite('image_thres1.png', thresh)
cv2.imshow('Detect image', img_copy)
cv2.imwrite('Contour Image.png', img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()