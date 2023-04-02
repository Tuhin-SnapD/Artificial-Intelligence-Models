""" 
This code captures video from the default camera, converts each frame to the HSV color space, and displays it in a window called 
"image." It also sets up a mouse event callback function that allows the user to click on a point in the displayed frame and print 
the upper and lower HSV limits of the pixel at that location.

The loop continues to capture and display frames until the user presses the 'q' key. Finally, the code releases the video capture 
object and closes the window.
 """

# Import Modules
import cv2
import numpy as np

# Capture video from the default camera
cap = cv2.VideoCapture(0)

# Read the current frame
ret, frame = cap.read()

# Convert the frame to HSV
hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# Define the callback function for mouse events
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = hsv_frame[y, x]
        hue = pixel[0]
        hue_range = 10
        lower = np.array([hue - hue_range, 100, 100])
        upper = np.array([hue + hue_range, 255, 255])
        print("Lower limit:", lower)
        print("Upper limit:", upper)

# Create a window and set the mouse callback function
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)

while True:
    # Read the current frame
    ret, frame = cap.read()
    
    # Convert the frame to HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Display the frame
    cv2.imshow('image', frame)

    # Wait for a key event
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# Release the video capture object and close the window
cap.release()
cv2.destroyAllWindows()
