import cv2
import numpy as np

vid = cv2.VideoCapture("testvid.mp4")
    # write a video
frame_height = int(vid.get(4))
frame_width = int(vid.get(3))
frame_size = (frame_width, frame_height)
fps = 20.0
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter('output2.mp4', fourcc, fps, frame_size)
while(vid.isOpened()):
    ret, frame = vid.read()
    if ret == True:
        output.write(frame)
        cv2.imshow('Frame', frame)
        k = cv2.waitKey(20)
        if k == ord('q'): # enter q to exist
            break  
    else:
        print('Stream disconnected')
        break

output.release()
cv2.destroyAllWindows()

#VideoWriter_fourcc('M', 'J', 'P', 'G') in Python.
