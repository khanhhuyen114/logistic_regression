import cv2
import numpy as np

img = cv2.imread('Sources/pic12.png')
# top_left_corner = []
# bottom_right_corner = []

# def draw_rectangle(action, x, y, flags, *userdata):
#     global top_left_corner, bottom_right_corner
#     if action == cv2.EVENT_LBUTTONDOWN:
#         top_left_corner = [(x, y)]
    
#     elif action == cv2.EVENT_LBUTTONUP:
#         bottom_right_corner = [(x,y)]
#         cv2.rectangle(img, top_left_corner[0], bottom_right_corner[0], (250,0,0),2, 8)
#         cv2.imshow("Window", img)
#         cv2.waitKey(0)

# cv2.namedWindow('Window')
# cv2.setMouseCallback('Window', draw_rectangle)
# temp = img.copy()
# k = 0
# if k!= 'q':
#     cv2.imshow("Window", img)
#     k = cv2.waitKey(0)
# # If c is pressed, clear the window, using the dummy image
# if (k == 99):
#     image= temp.copy()
#     cv2.imshow("Window", image)

#
maxScaleUp = 100
scaleFactor = 1
windowName = "Resize Image"
trackbarValue = "Scale"
cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)
 
def scaleImage(*args):
    # Get the scale factor from the trackbar 
    scaleFactor = 1+ args[0]/100.0
    # Resize the image
    scaledImage = cv2.resize(img, None, fx=scaleFactor, fy = scaleFactor, interpolation = cv2.INTER_LINEAR)
    cv2.imshow(windowName, scaledImage)
 
# Create trackbar and associate a callback function
cv2.createTrackbar(trackbarValue, windowName, scaleFactor, maxScaleUp, scaleImage)
 
# Display the image
cv2.imshow(windowName, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
