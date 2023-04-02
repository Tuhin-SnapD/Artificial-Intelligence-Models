""" 
This code captures frames from a video stream, detects the presence of a specific color (red in this case) in each frame, and tracks 
the movement of the colored object in real-time. It then prints the position and size of the object, and gives instructions to move 
forward, turn left or right, or stop, depending on the location of the object in the frame.

More specifically, the code initializes the camera and sets the boundaries for detecting the red color in the frame. It then applies 
various image processing techniques like resizing, blurring, and thresholding to remove noise and enhance the image. It then finds 
contours in the mask and selects the largest contour, representing the colored object. It calculates the center and radius of the 
object, and based on their values, gives instructions to move the object. Finally, it displays the original frame with the object 
tracked, and waits for user input to terminate the program. 
"""

# Import Modules
import imutils
import cv2

# Define the lower and upper boundaries for detecting color in HSV color space
# Please note only the first value changes. Lower-(X, 100, 100) and Upper- (Y, 255,255)
lower = (100, 100, 100)
upper = (120, 255, 255)
# This can be obtained from hsv_value_range.py

# Initialize the camera
camera = cv2.VideoCapture(0)

while True:
    # Capture a frame from the camera
    grabbed, frame = camera.read()

    # Resize the frame
    frame = imutils.resize(frame, width=900)

    # Apply Gaussian blur to the frame
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    # Create a mask for the color
    mask = cv2.inRange(hsv, lower, upper)

    # Erode and dilate the mask to remove noise
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Find the contours in the mask
    contours = cv2.findContours(
        mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)

    # Initialize the center of the object to be None
    center = None

    # If contours are found
    if len(contours) > 0:
        # Find the largest contour in the mask
        c = max(contours, key=cv2.contourArea)

        # Get the minimum enclosing circle and centroid of the largest contour
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        # If the radius of the enclosing circle is greater than 10 pixels
        if radius > 10:
            # Draw the circle and centroid on the frame
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

            # Print the center and radius of the enclosing circle
            print(center, radius)

            # If the radius is greater than 250 pixels, stop
            if radius > 250:
                print("Stop")
            else:
                # If the center of the object is to the left of the frame, turn left
                if center[0] < 150:
                    print("Left")
                # If the center of the object is to the right of the frame, turn right
                elif center[0] > 450:
                    print("Right")
                # If the object is in the center of the frame, move forward
                elif radius < 250:
                    print("Front")
                # If the object is too close, stop
                else:
                    print("Stop")

    # Show the frame
    cv2.imshow("Frame", frame)

    # Wait for key press
    key = cv2.waitKey(1) & 0xFF

    # If the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break

# Release the camera and destroy all windows
camera.release()
cv2.destroyAllWindows()
