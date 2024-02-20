import mediapipe as mp
import cv2
import csv
import numpy as np


mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

class_name = "lateral_raise"


cap = cv2.VideoCapture('lateralRaise_woman.mp4')

if cap is True:
    print("video is found!")

else:
    print("video not found")

frame_list = []

with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            print("the frame is empty")
            break
        #recoloring feed to make it passable to mediapipe
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False



        results = holistic.process(image)


        try:
            pose = results.pose_landmarks.landmark
            pose_row = list(np.array([[landmark.x, landmark.y, landmark.z, landmark.visibility] for landmark in pose]).flatten())

            #redudent detection of face landmarks....may come in use later specifically for detecting strikes to the dome
            face = results.face_landmarks.landmark
            face_row = list(np.array([[landmark.x, landmark.y, landmark.z, landmark.visibility] for landmark in face]).flatten())

            row = pose_row+face_row

            row.insert(0, class_name)

            with open('coords.csv', mode='a', newline='') as f:
                csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow(row)

        except :
            pass

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()

print("Job is done, check coords.csv")