import cv2
import numpy as np

img = cv2.imread('Sources/pic10_1.png', cv2.IMREAD_GRAYSCALE)
# Detect point
# params = cv2.SimpleBlobDetector_Params()
# detector = cv2.SimpleBlobDetector_create()
# keypoint = detector.detect(img)


# Detect by area
params = cv2.SimpleBlobDetector_Params()
# params.filterByArea = True
# params.minArea = 100

# # by Circularity
# params.filterByCircularity = True
# params.minCircularity = 0.9

# # by Convexity
# params.filterByConvexity = True
# params.minConvexity = 0.2

# # by inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01
detector = cv2.SimpleBlobDetector_create(params)
keypoint = detector.detect(img)
keypoint_img = cv2.drawKeypoints(img,keypoint, np.array([]), (0,250,0), cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)
cv2.imshow('Key point image', keypoint_img)
cv2.waitKey()

