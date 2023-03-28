import serial
import time
import cv2
import time
from cvzone.HandTrackingModule import HandDetector

serialcomm = serial.Serial('COM8', 115200)
serialcomm.timeout = 1
detector = HandDetector(maxHands=1,
                        detectionCon=0.8)

detector = HandDetector(maxHands=1,
                        detectionCon=0.8)
  
# it detect only one hand from
# video with 0.8 detection confidence
video = cv2.VideoCapture(0)
  
# it detect only one hand from
# video with 0.8 detection confidence
video = cv2.VideoCapture(0)

def main():
    while True:
        _, img = video.read()
        img = cv2.flip(img, 1)
      
        # Find the hand with help of detector
        hand = detector.findHands(img, draw=False)
      
        # Here we take img by default if no hand found
        fing = cv2.imread("FingerGesture/0.png")
        #i = input("input(on/off): ").strip().capitalize()
        # if i == 'done':
        #     print('finished program')
        #     break
        i = "0"
        if hand:
        
          # Taking the landmarks of hand
            lmlist = hand[0] 
            if lmlist:
            
            # Find how many fingers are up
            # This function return list
                fingerup = detector.fingersUp(lmlist)  
              
            # Change image based on 
            # different-different cononditions
                if fingerup == [0, 1, 0, 0, 0]:
                   fing = cv2.imread("FingerGesture/1.png")
                   i = "1"
                if fingerup == [0, 1, 1, 0, 0]:
                   fing = cv2.imread("FingerGesture/2.png")
                   i = "2"
                if fingerup == [0, 1, 1, 1, 0]:
                    fing = cv2.imread("FingerGesture/3.png")
                    i="3"                
                if fingerup == [0, 1, 1, 1, 1]:
                    fing = cv2.imread("FingerGesture/4.png")
                    i="4"
                if fingerup == [1, 1, 1, 1, 1]:
                    fing = cv2.imread("FingerGesture/5.png")
                    i="5"
         # Resize the image
        fing = cv2.resize(fing, (220, 280))
        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
          # Place the image in main frame
        img[50:330, 20:240] = fing
        
        serialcomm.write(i.encode())
        time.sleep(0.5)
        print(serialcomm.readline().decode('ascii'))

    serialcomm.close()
    
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()