import cv2
import face_recognition as FR
import random

class Reg():
    def __init__(self):
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    def pic1(self):
        while True:
            igs, frame = self.cam.read()
            rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            faceLoc = FR.face_locations(rgbFrame)
            frame2=frame.copy()

            for face in faceLoc:
                top, right, bottom, left = face
                cv2.rectangle(frame2, (left, top), (right, bottom), (255, 0, 0), 2)
                cv2.putText(frame2, "Press(1,2,3)", (left, top - 10), self.font, .75, (255, 0, 255), 2)
            cv2.imshow('pics2', frame2)
            key = cv2.waitKey(1) & 0xff
            if key == ord("1"):
                self.cam.release()
                cv2.destroyAllWindows()
                return [frame,"1"]

            elif key == ord("2"):
                self.cam.release()
                cv2.destroyAllWindows()
                return [frame,"2"]

            elif key == ord("3"):
                self.cam.release()
                cv2.destroyAllWindows()
                return [frame,"3"]

# reg=Reg()
# reg.pic1()