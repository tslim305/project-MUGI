import mediapipe as mp
import cv2
import csv 
import numpy as np
import pandas as pd


'''Loading up model and visulization tools'''
mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils



'''Setting up CSV file for coordinates'''
num_coords = 501 #magic number that is derived from len(results.pose_landmarks.landmark)+len(results.face_landmarks.landmark). Done for conovininence


landmarks = ['class']
for val in range(1, num_coords+1):
    landmarks += ['x{}'.format(val), 'y{}'.format(val), 'z{}'.format(val), 'v{}'.format(val)]

with open('jab_cross_coords.csv', mode='w', newline='') as f:
    csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(landmarks)


print("starting data proccessing")

'''getting coordinates for jab'''

class_name = "jab_orthodox"
#this is variable is use to cycle through videos in directory 
vid_num = 1
vid_root = "jab/jab_orthodox/vid"


while vid_num <= 3:

    vid_path = vid_root + str(vid_num) +".mov"
    cap = cv2.VideoCapture(vid_path)

    frame_list = []

    with mp_holistic.Holistic(min_detection_confidence=0.65, min_tracking_confidence=0.65) as holistic:
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

                with open('jab_cross_coords.csv', mode='a', newline='') as f:
                    csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    csv_writer.writerow(row)

            except :
                pass

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break


    cap.release()
    cv2.destroyAllWindows()

    vid_num += 1


class_name = "jab_southpaw"
#this is variable is use to cycle through videos in directory 
vid_num = 1
vid_root = "jab/jab_southpaw/vid"


while vid_num <= 3:

    vid_path = vid_root + str(vid_num) +".mov"
    cap = cv2.VideoCapture(vid_path)

    frame_list = []

    with mp_holistic.Holistic(min_detection_confidence=0.65, min_tracking_confidence=0.65) as holistic:
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

                with open('jab_cross_coords.csv', mode='a', newline='') as f:
                    csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    csv_writer.writerow(row)

            except :
                pass

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break


    cap.release()
    cv2.destroyAllWindows()

    vid_num += 1

print("done getting data for jabs. Moving on to Cross")
'''Getting coordinates for Cross'''

class_name = "cross_orthodox"
#this is variable is use to cycle through videos in directory 
vid_num = 1
vid_root = "cross/cross_orthodox/vid"


while vid_num <= 3:

    vid_path = vid_root + str(vid_num) +".mov"
    cap = cv2.VideoCapture(vid_path)

    frame_list = []

    with mp_holistic.Holistic(min_detection_confidence=0.65, min_tracking_confidence=0.65) as holistic:
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

                with open('jab_cross_coords.csv', mode='a', newline='') as f:
                    csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    csv_writer.writerow(row)

            except :
                pass

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break


    cap.release()
    cv2.destroyAllWindows()

    vid_num += 1


class_name = "cross_southpaw"
#this is variable is use to cycle through videos in directory 
vid_num = 1
vid_root = "cross/cross_southpaw/vid"


while vid_num <= 3:

    vid_path = vid_root + str(vid_num) +".mov"
    cap = cv2.VideoCapture(vid_path)

    frame_list = []

    with mp_holistic.Holistic(min_detection_confidence=0.65, min_tracking_confidence=0.65) as holistic:
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

                with open('jab_cross_coords.csv', mode='a', newline='') as f:
                    csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    csv_writer.writerow(row)

            except :
                pass

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break


    cap.release()
    cv2.destroyAllWindows()

    vid_num += 1


print("data proccessing done")






