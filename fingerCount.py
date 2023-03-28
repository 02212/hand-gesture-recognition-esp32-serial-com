# import cv2
# import time
# import os

# wCam, hCam = 640, 480

# cap = cv2.VideoCapture(0)
# cap.set(3, wCam)
# cap.set(4, hCam)
# path = "FingerGesture"
# picList = os.listdir(path)
# print(picList)
# overlayList = []
# for imgPath in picList:
#     image = cv2.imread(f'{path}/{imgPath}')
#     overlayList.append(image)

# print(len(overlayList))

# while True:
#     success, img = cap.read()
#     img[0:512, 0:512] = overlayList[0]
#     cv2.imshow('Image', img)
#     cv2.waitKey(1)


# import libraries and required classes
import cv2
import time
from cvzone.HandTrackingModule import HandDetector


# declaring HandDetector with
# some basic requirements
detector = HandDetector(maxHands=1,
                        detectionCon=0.8)
  
# it detect only one hand from
# video with 0.8 detection confidence
video = cv2.VideoCapture(0)
password = ""
while True:
      # Capture frame-by-frame 
    _, img = video.read()
    img = cv2.flip(img, 1)
      
    # Find the hand with help of detector
    hand = detector.findHands(img, draw=False)
      
    # Here we take img by default if no hand found
    fing = cv2.imread("FingerGesture/0.png")
    password += "0"
    if hand:
        
          # Taking the landmarks of hand
        lmlist = hand[0] 
        if lmlist:
            
              # Find how many fingers are up
            # This function return list
            fingerup = detector.fingersUp(lmlist)  
              
            # Change image based on 
            # different-different conditions
            if fingerup == [0, 1, 0, 0, 0]:
                fing = cv2.imread("FingerGesture/1.png")
                password += "1"
            if fingerup == [0, 1, 1, 0, 0]:
                fing = cv2.imread("FingerGesture/2.png")
                password += "2"
            if fingerup == [0, 1, 1, 1, 0]:
                fing = cv2.imread("FingerGesture/3.png")
                password += "3"
            if fingerup == [0, 1, 1, 1, 1]:
                fing = cv2.imread("FingerGesture/4.png")
                
            if fingerup == [1, 1, 1, 1, 1]:
                fing = cv2.imread("FingerGesture/5.png")
                password += "5"
    # Resize the image
    fing = cv2.resize(fing, (220, 280))
      
    # Place the image in main frame
    img[50:330, 20:240] = fing
    if len(password)<4:
        print((password))
    else:
        password = ""
    # Display the resulting frame
    
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
      
# When everything done, release
# the capture and destroy the windows
video.release()
cv2.destroyAllWindows()