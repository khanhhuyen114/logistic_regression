import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils

mp_pose = mp.solutions.pose

def calculate_angle(a,b,c):
    a, b, c = np.array(a), np.array(b),  np.array(c)

    radians = np.arctan2(c[1]- b[1], c[0]-b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180/np.pi)
    if angle > 180:
        angle = 360 - 180
    return angle

counter = 0
#Read Video
cap = cv2.VideoCapture('Sources/vid_detect.mp4')
with mp_pose.Pose(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as pose:
    while(cap.isOpened()):
        ret, frame = cap.read()
        # Change from BGR to RGB
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img.flags.writeable = False

        #Make detection
        result = pose.process(img)

        # Back the original color channels
        img.flags.writeable = True
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        #Extract landmarks 
        try:
            landmarks = result.pose_landmarks.landmark
            #print(landmarks)
        except:
            pass
        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].visibility
        #Render detection
        mp_drawing.draw_landmarks(img, result.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                ) 
        
        # calculate_angle
        # Landmarks: là 1 list chứa tọa độ 33 điểm trên cơ thế
        # mp_pose.PoseLandmark.LEFT_SHOULDER.value: index của vai trái trong landmark

        shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
        elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
        wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
        angle = calculate_angle(shoulder, elbow, wrist)
        angle_st = "{:.2f}".format(angle)
        #Visualize angle: put text 
        cv2.putText(img, angle_st, tuple(np.multiply(elbow, [640,512]).astype(int)), 2, 0.5, (250,250,250),2, lineType = cv2.LINE_AA)
        
        # Curl counter
        
        if angle > 150:
            stage = 'stretch'
        if angle < 100 and stage == 'stretch':
            counter += 1
            stage = 'shrink'
        
        # Visualize counter
        cv2.rectangle(img, (0,0), (130, 70), (80,30,20), -1)
        cv2.putText(img, 'REPS', (20,25),2, 1, (250,250,250),2, lineType = cv2.LINE_AA )
        cv2.putText(img, str(counter), (50,60),2, 1, (250,250,250),2, lineType = cv2.LINE_AA )
        cv2.imshow('Mediapipe Vid', img)             
        k = cv2.waitKey(20)
        if k == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
        

