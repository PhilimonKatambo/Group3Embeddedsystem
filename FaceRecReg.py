import cv2
import face_recognition as FR
import random

class Reg():
    def __init__(self):
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)

    def pic1(self):
        while True:
            igs, frame = self.cam.read()
            igs2, frame2 = self.cam.read()
            rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            faceLoc = FR.face_locations(rgbFrame)

            for face in faceLoc:
                top, right, bottom, left = face
                cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)
            cv2.putText(frame, "Press(Q)", (left, top - 10), self.font, .75, (255, 0, 255), 2)
            cv2.imshow('pics2', frame)
            if cv2.waitKey(1) == ord("q"):
                self.cam.release()
                cv2.destroyAllWindows()
                num=random.randint(1,100)
                cv2.imwrite(f'./registeredPics/{str(num)}.jpg', frame)
                return

reg=Reg()
reg.pic1()