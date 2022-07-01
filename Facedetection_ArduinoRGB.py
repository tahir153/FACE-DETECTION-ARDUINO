# RGB
import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject


cap = cv2.VideoCapture(1)
detector = FaceDetector()
arduino = SerialObject("COM6")
while True:
    success , img = cap.read()
    img,bboxs = detector.findFaces(img)

    if bboxs:
        arduino.sendData([1,0,1])
    else:
        arduino.sendData([0,1,1])

    cv2.imshow("Image",img)
    if cv2.waitKey(10) == ord("q"):.
        break