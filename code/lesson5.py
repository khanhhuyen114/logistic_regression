import cv2
import numpy as np

img = cv2.imread('./Sources/testpic.png',1)
# ROTATE AN IMAGE
# height, width = img.shape[:2]

# center_point = (width/2, height/2)

# rotate_matrix = cv2.getRotationMatrix2D(center_point, 90, 1)

# rotate_img = cv2.warpAffine(img, rotate_matrix, (width, height))

# cv2.imshow("Origin Image", img)
# cv2.imshow('Rotate Image', rotate_img)
# cv2.waitKey(0)
# cv2.imwrite('Sources/rotate_img.png', rotate_img)

# TRANSLATION AN IMAGE
height, width = img.shape[:2]
tx, ty = width/4, height/4
trans_matrix = np.array([[1, 0, tx], 
                        [0, 1, ty]])
trans_img = cv2.warpAffine(img, trans_matrix, (width, height))
cv2.imshow("Origin Image", img)
cv2.imshow('Translation Image', trans_img)
cv2.waitKey(0)
cv2.imwrite('Sources/translation_img.png', trans_img)


cv2.destroyAllWindows