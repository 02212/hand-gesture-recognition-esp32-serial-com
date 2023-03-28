import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

prevTime = 0
curTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for indexhandsLms in results.multi_hand_landmarks:
            for id, lm in enumerate(indexhandsLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                #if id == 12:
                cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
                mpDraw.draw_landmarks(img, indexhandsLms, mpHands.HAND_CONNECTIONS)

    curTime = time.time()
    frames = 1/(curTime - prevTime)
    prevTime = curTime


    cv2.putText(img, str(int(frames)), (10,70), cv2.FONT_HERSHEY_PLAIN,2, (255,50,120),3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
