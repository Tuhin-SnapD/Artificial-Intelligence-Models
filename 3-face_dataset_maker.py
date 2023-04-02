""" 
This is a Python code that uses OpenCV to capture 30 images of a user's face using the webcam, and saves them in a directory named 
"snapd" inside the "dataset" directory. It uses the Haar cascade classifier to detect the user's face in each image and crops and 
resizes the face to a fixed size of 130x100 pixels before saving it. The captured images can be used as training data for face 
recognition models.

Note that the code also checks if the "dataset" and "snapd" directories exist and creates them if they don't. It also displays each 
captured image with the detected face rectangle drawn on it in a window named "FaceDetection". The loop stops after 30 images have 
been captured or when the user presses the Esc key.
"""

# Import the required libraries
import cv2
import os

# set the name of the directory to save the images and the subdirectory for the user's images
dataset = "dataset"
name = "snapd"

# # create the 'dataset' directory if it doesn't exist
if not os.path.isdir(dataset):
    os.mkdir(dataset)

# create the 'snapd' directory inside the 'dataset' directory
path = os.path.join(dataset, name)
if not os.path.isdir(path):
    os.mkdir(path)

# set the size of the cropped face images and load the Haar cascade classifier for face detection
(width, height) = (130, 100)
alg = r"dataset/haarcascade_frontalface_default.xml"
haar_cascade = cv2.CascadeClassifier(alg)

# initialize the webcam and start capturing images
cam = cv2.VideoCapture(0)

# set the count of images captured to 1
count = 1

# start a loop to capture 30 images
while count < 31:
    print(count)
    # read a frame from the webcam
    _, img = cam.read()

    # convert the frame to grayscale for face detection
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # use the Haar cascade classifier to detect faces in the grayscale image
    face = haar_cascade.detectMultiScale(grayImg, 1.3, 4)

    # loop through the detected faces and crop and resize them to the desired size
    for (x, y, w, h) in face:
        # draw a rectangle around the detected face
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # crop the face region from the grayscale image
        faceOnly = grayImg[y:y+h, x:x+w]
        # resize the cropped face image to the desired size
        resizeImg = cv2.resize(faceOnly, (width, height))
        # save the resized face image to the specified path
        cv2.imwrite("%s/%s.jpg" % (path, count), resizeImg)
        count += 1  # increment the count of images captured

    # display the captured image with the detected face rectangles drawn on it
    cv2.imshow("FaceDetection", img)

    # wait for a key press and check if the user pressed the Esc key to exit the loop
    key = cv2.waitKey(10)
    if key == 27:
        break

# print a message indicating that the images have been captured successfully
print("Image Captured succssfully")

# release the webcam and close all windows
cam.release()
cv2.destroyAllWindows()