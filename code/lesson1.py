import cv2
import numpy as np
from matplotlib import pyplot as plt


print(cv2.__version__)
img = cv2.imread('Sources/testpic.png',-1)
print(img)
cv2.imshow('Display Image', img)
cv2.waitKey(0)
cv2.imwrite('testpic_copy.png', img)
cv2.destroyAllWindows()
