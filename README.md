# Face Authorization / Recognition python code
### These python codes are to create dataset, encode dataset, and perform facial recognition using encoded file.

### 1. trydatacreation.py :
#### Libraries Required: opencv-python, numpy
#### This is used to automatically capture cv2 frame when the face is detected using *haarcascade_frontalface_default.xml*
#### The dataset folder with the name dataset would be create
#### The images would be stored with random name inside the dataset in .jpg format
#### The image only captures 5 photos of the person when the face is detected
#### The amount of frames to be captured can be changed

### 2. encode_generator.py
#### Libraries Required : opencv-python, face_recognition, dlib, cmake, setuptools, pickle 
#### This python code is to encode the images
#### In this python code, face in the images inside the dataset folder is encoded and stored inside a multidimensional array
#### Further, converted into a pickle file

If you encounter any errors downloading face_recognition, dlib or cmake scroll the bottom of this readme file.

### 3. trypythonrec.py
#### Libraries Required : opencv-python, face_recognition, dlib, cmake, setuptools, pickle, dateandtime
#### This python is the main code which is used for authentication
#### This code compares the current face in the frame to the face encodings stored in the pickle file
#### I will add more versions of this code depending on the purpose into the repository later for e.g I would like to add a function in this code to store the name of the person recognized and time in a text log file even when the person is not recognized the python would add the unknown label instead of person name

### Resource files 

#### These contain modes to display in the cv frame, and you are free to seek help regarding the removal or change of resources on my linkedin.


### Handling Library Install Errors: 
1. cmake error: For the cmake error, even if you install the cmake library from python it would not be enough to install the dlib. So, we need to install visual studio (not visual studio code) and inside that we need to select Desktop Development With C++ and install.

![image](https://github.com/therealhimanshu/FaceAuthorizationPythonAndArduino/assets/102641944/f36e6c13-b6f2-4413-9c66-42c0919c253f)

If you already have visual studio installed, you can modify no worry.
This would resolve the cmake error. Now installing dlib would not be a problem and if dlib is installed successfully, then you would not encounter anymore error installing face_recognition. If you are still facing any error, reach me out on my linkedin.

### My Linkedin: *https://linkedin.com/in/himanshujoshidevelops/* 
