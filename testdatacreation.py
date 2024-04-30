import os
import cv2
import numpy as np
import random
import string

# Initialize camera
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Load pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to save image in the dataset folder with a unique filename
def save_image(frame, dataset_path):
    # Generate a random filename
    while True:
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6)) + '.jpg'
        image_path = os.path.join(dataset_path, filename)
        if not os.path.exists(image_path):
            cv2.imwrite(image_path, frame)
            print("Image captured and saved as:", filename)
            break

# Create dataset directory if it doesn't exist
dataset_path = 'dataset'
if not os.path.exists(dataset_path):
    os.makedirs(dataset_path)

# Variable to count captured frames
frame_count = 0

while True:
    # Read frame from camera
    ret, frame = cap.read()

    # Convert frame to grayscale for face detection
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

    # Capture frames when a face is detected
    if len(faces) > 0:
        frame_count += 1
        # Change the value from 5 to number of frames you want to capture
        if frame_count <= 5:
            save_image(frame, dataset_path)
        else:
            print("Captured 5 frames.")
            break

    # Display text only when a face is detected
    if len(faces) > 0:
        cv2.putText(frame, "Face Detected", (20, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('Capture Image', frame)

    # Save the frame when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
