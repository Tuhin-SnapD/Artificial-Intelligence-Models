""" 
Motion Detection using OpenCV

This code is using OpenCV library to detect motion in real-time video captured from a camera. It does this by comparing each frame of video to the 
first frame captured, and detecting any changes that occur. When motion is detected, the program highlights the moving object with a green 
rectangle and displays a message on the screen indicating that motion has been detected. The program runs until the user presses the 'q' key to 
quit.

This program uses a background subtraction algorithm to detect motion in a video stream. Specifically, it compares the current frame of the video 
to the first frame (which is stored as the background), and then applies a series of image processing steps to detect any changes or motion in the 
scene. The algorithm uses Gaussian blur, thresholding, and contour detection to identify and highlight the regions of the image where motion is 
detected.
"""

# Install Necessary Packages
import cv2
import time
import imutils

def detect_motion(cam, area=500):
    # Initialize the first frame to None
    firstFrame = None
    while True:
        try:
            # Capture a frame from the camera
            _, img = cam.read()
            # Set initial text to "Normal"
            text = "Normal"
            # Resize the frame
            img = imutils.resize(img, width=500)
            # Convert the frame to grayscale
            grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Apply Gaussian blur to the grayscale frame
            gaussianImg = cv2.GaussianBlur(grayImg, (21, 21), 0)


            # If the first frame is None, set it to the current frame and continue to the next iteration
            if firstFrame is None:
                    firstFrame = gaussianImg
                    continue
            
            # Compute the absolute difference between the first frame and the current frame
            imgDiff = cv2.absdiff(firstFrame, gaussianImg)
            # Apply thresholding to the difference image to create a binary image
            threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1]
            # Dilate the thresholded image to fill in gaps
            threshImg = cv2.dilate(threshImg, None, iterations=2)
            # Find contours in the thresholded image
            cnts = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            # Extract the contours
            cnts = imutils.grab_contours(cnts)
            
            # Loop over the contours
            for c in cnts:
                    # If the contour area is less than the minimum area, skip it
                    if cv2.contourArea(c) < area:
                            continue
                    # Compute the bounding box for the contour and draw it on the frame
                    (x, y, w, h) = cv2.boundingRect(c)
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    # Set the text to "Moving Object detected"
                    text = "Moving Object detected"
            
            # Print the text
            print(text)
            # Draw the text on the frame
            cv2.putText(img, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            # Show the frame
            cv2.imshow("cameraFeed",img)
            
            # Wait for a key press and check if it's "q"
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
        
        # Handle any exceptions and break out of the loop
        except Exception as e:
            print(e)
            break

# Open the default camera
cam = cv2.VideoCapture(0)
# Sleep for a second to allow the camera to warm up
time.sleep(1)
# Call the detect_motion function
detect_motion(cam)

cv2.destroyAllWindows()