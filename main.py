import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode = False, maxHands = 2, detectionCon = 0.5, trackCon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for indexhandsLms in self.results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(img, indexhandsLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPos(self, img, handNo=8, draw = True):
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(indexhandsLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)
                lmList.append([id,cx,cy])
                # if id == 12:
                if draw:
                    cv2.circle(img, (cx, cy), 7, (255, 0, 255), cv2.FILLED)
        return lmList

def main():
    prevTime = 0
    curTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPos(img)
        if len(lmList) !=0:
            print(lmList[4])
        curTime = time.time()
        frames = 1 / (curTime - prevTime)
        prevTime = curTime


    cv2.putText(img, str(int(frames)), (10,70), cv2.FONT_HERSHEY_PLAIN,2, (255,50,120),3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)


if __name__ == "__main__":
    main()