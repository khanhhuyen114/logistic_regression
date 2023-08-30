import cv2
import numpy as np

vid = cv2.VideoCapture('Sources/vid14.mp4')
framesId = vid.get(5) * np.random.uniform(size = 25)
frames = []
for fid in framesId:
    vid.set(cv2.CAP_PROP_POS_FRAMES, fid) # thay thế giá trị cv2.Cap_pro.. = fid
    ret, frame = vid.read()
    frames.append(frame)

# Calculate the median
medianFrame = np.median(frames, axis = 0).astype(dtype=np.uint8)  
#cv2.imshow('Frame'_med, medianFrame)
cv2.waitKey(0)

# FRAME DIFFERENT
vid.set(cv2.CAP_PROP_POS_FRAMES, 0)
gray_med_frame = cv2.cvtColor(medianFrame, cv2.COLOR_BGR2GRAY)
ret = True
while(ret):
    ret, frame = vid.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    dframe = cv2.absdiff(frame, gray_med_frame)
    th, dframe = cv2.threshold(dframe, 40, 255, cv2.THRESH_BINARY)
    cv2.imshow('Frame', dframe)
    k = cv2.waitKey(20)
    if k == ord('q'): # enter q to exist
            break  

vid.release()
cv2.destroyAllWindows()