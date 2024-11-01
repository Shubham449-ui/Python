import cv2
import mediapipe as mp
import numpy as np

cap = cv2.VideoCapture(0)

mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils
pose = mp_pose.Pose()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    result = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    if result.pose_landmarks:
        mp_draw.draw_landmarks(frame, result.pose_landmarks,mp_pose.POSE_CONNECTIONS)
        h,w,c = frame.shape
        opImg = np.zeros([h,w,c])
        opImg.fill(0)
        mp_draw.draw_landmarks(opImg, result.pose_landmarks,mp_pose.POSE_CONNECTIONS)
        cv2.imshow("Extract image",opImg)


    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)
    print(result.pose_landmarks)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
