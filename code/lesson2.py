import cv2
import numpy as np

vid = cv2.VideoCapture('Sources/testvid.mp4')          # read video from a file
#vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)      # read video from webcam
#vid = cv2.VideoCapture('testvid%04d.jpg')     # read video from image sequences
if vid.isOpened() ==  False:
    print('Error opening the video')
else:
    fps = vid.get(5)
    print(f'Frame per second: {fps} fps')
    frame_count = vid.get(7)
    print(f'Frame count: {frame_count}')

while(vid.isOpened()):
    ret, frame = vid.read()
    if ret == True:
        cv2.imshow('Frame', frame)
        k = cv2.waitKey(20)
        if k == ord('q'): # enter q to exist
            break
    else:
        break

vid.release()
cv2.destroyAllWindows()

# write a video
frame_height = vid.get(4)
frame_width = vid.get(3)
frame_size = (frame_width, frame_height)
fps = 20
#VideoWriter_fourcc('M', 'J', 'P', 'G') in Python.

