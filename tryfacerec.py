import cv2
import os
import face_recognition
import numpy as np
import pickle
import time

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread('resources/bg-img.png')

folderModePath = 'resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []

for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))


file = open('EncodeFile.p', 'rb')
encodeListKnownWithNames = pickle.load(file)
file.close()
encodeListKnown, person_name = encodeListKnownWithNames


modeType = 0
counter = 0
id = -1


signal = '0'

start_time = time.time()  

while time.time() - start_time <= 10: 
    success, img = cap.read()

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurrFrame = face_recognition.face_locations(imgS)
    encodeCurrFrame = face_recognition.face_encodings(imgS, faceCurrFrame)
    
    imgBackground[120:120+480, 70:70+640] = img
    imgBackground[410:410+150, 800:800+350] = imgModeList[modeType]
    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray_frame = cv2.cvtColor(imgBackground, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for encodeFace, faceLoc in zip(encodeCurrFrame, faceCurrFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        matchIndex = np.argmin(faceDis)
        if matches[matchIndex] and faceDis[matchIndex] < 0.5:
            y1, x2, y2, x1 = faceLoc
            color = (0, 255, 0)
            cv2.rectangle(imgBackground, (x1*4+70, y1*4+120), (x2*4+70, y2*4+120), color, 2)
            signal = '1'
            id = matchIndex
            cv2.putText(imgBackground, "Welcome!", (860, 230),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            if(time.time()- start_time>5):
                print("Recognized")
                cap.release()
                cv2.destroyAllWindows()
                exit()
        else:
            color = (0,0,255)            
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(imgBackground, (x1+70, y1+120), (x2+70, y2+120), color, 2)

        

    cv2.imshow("System.exe", imgBackground)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
print("Unrecognized")
