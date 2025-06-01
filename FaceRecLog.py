import cv2
import face_recognition as FR
from pathlib import Path

class Login():
    def __init__(self):
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        pics1 = list(Path('./registeredPics').glob('*.jpg'))
        pics2 = list(Path('./registeredPics').glob('*.png'))

        self.pics = pics1 + pics2

        # self.arduino = serial.Serial('COM6', 9600)
        # time.sleep(2)
        # self.arduino.write("1\n".encode())

    def logs(self):

        if len(self.pics) == 0:
            print("No pics init\n")
        else:
            picEncs = []
            frame_count = 0
            process_every = 5

            for pic in self.pics:
                img = cv2.imread(str(pic), 1)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                imgFLoc = FR.face_locations(img)
                imgEncs = FR.face_encodings(img, imgFLoc)
                picEncs.append(imgEncs)
            while True:
                igs, frame = self.cam.read()

                frame_count+=1
                rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                faceLoc = FR.face_locations(rgbFrame)
                faceEncs = FR.face_encodings(rgbFrame, faceLoc)
                matches = []
                for (face, faceEnc) in zip(faceLoc, faceEncs):
                    top, right, bottom, left = face
                    cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)

                    matched_name="Unknown"
                    roomNum = "0"
                    for i, picEnc in enumerate(picEncs):
                        match = FR.compare_faces(picEnc, faceEnc, tolerance=0.3)
                        if True in match:
                            matched_name = self.pics[i].name[:-6]
                            roomNum=str(self.pics[i].name[-5:-4])
                            break

                    if matched_name!="Unknown":
                        cv2.putText(frame, matched_name, (left, top - 10), self.font, .75, (255, 0, 255), 2)
                        cv2.putText(frame, "Press(1,2,3)", (left + 100, top - 10), self.font, .75, (255, 0, 255), 2)

                        key = cv2.waitKey(1) & 0xff
                        if key == ord('1'):
                            self.cam.release()
                            cv2.destroyAllWindows()
                            if roomNum=="1":
                                print("1")
                                return True
                            else:
                                return False

                        elif key == ord('2'):
                            self.cam.release()
                            cv2.destroyAllWindows()
                            if roomNum=="2":
                                return True
                            else:
                                return False

                        elif key == ord('3'):
                            self.cam.release()
                            cv2.destroyAllWindows()
                            if roomNum=="3":
                                return True
                            else:
                                return False

                    else:
                        cv2.putText(frame, "Unknown", (left, top - 10), self.font, .75, (255, 0, 255), 2)
                        cv2.putText(frame, "Press(q)", (left + 100, top - 10), self.font, .75, (255, 0, 255), 2)
                        if cv2.waitKey(1) == ord('q'):
                            self.cam.release()
                            cv2.destroyAllWindows()
                            return False
                    # else:
                    #     cv2.putText(frame, "Unknown", (left, top - 10), self.font, .75, (255, 0, 255), 2)
                    #     cv2.putText(frame, "Press(Q)", (left + 100, top - 10), self.font, .75, (255, 0, 255), 2)
                    #     cv2.imshow('pics', frame)
                    #     if cv2.waitKey(1) == ord('q'):
                    #         self.cam.release()
                    #         cv2.destroyAllWindows()
                    #         return False

                if frame_count % process_every != 0:
                    cv2.imshow('Face Login', frame)
                    if cv2.waitKey(1) == ord('e'):
                        break
                    continue


# log = Login()
# log.logs()