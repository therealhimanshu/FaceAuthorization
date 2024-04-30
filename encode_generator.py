import cv2
import face_recognition
import pickle
import os

folderPath = 'Dataset'
pathList = os.listdir(folderPath)
# print(pathList)
imgList = []
person_name = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    # print(os.path.splitext(path)[0])
    person_name.append(os.path.splitext(path)[0])
print(person_name)

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(img)
        if len(face_locations) > 0:
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        else:
            print(f"No faces detected in image: {img}")
    return encodeList

print("Started")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithNames = [encodeListKnown, person_name]
print("Completed")

file = open('EncodeFile.p','wb')
pickle.dump(encodeListKnownWithNames, file)
file.close
print("file saved")