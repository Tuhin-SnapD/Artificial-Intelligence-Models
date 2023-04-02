""" 
This code loads an image using OpenCV, converts it to grayscale, resizes it, applies Gaussian blur and thresholding, and saves each 
processed image to a separate file in a dataset directory. The code then displays the original and processed images in separate 
windows using OpenCV.

After processing the images, the code opens the default camera and displays the live feed in a window called "Camera". The code loops 
over the frames from the camera until the "q" key is pressed, at which point the camera is released and all windows are closed.

Overall, this code demonstrates basic image processing and camera capture using OpenCV. 
"""

# Import necessary packages
import cv2
import imutils

# Load the image using OpenCV
img_original = cv2.imread("dataset/coding.png")

# Print image information
print("Shape: ", img_original.shape)
print("Size: ", img_original.size)
print("Type: ", img_original.dtype)

# Convert the image to grayscale
img_gray = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)

# Save the grayscale image as "gray_coding.png" using "cv2.imwrite()"
cv2.imwrite("dataset/bwImage.png", img_gray)

# Resize the image to a width of 200 pixels
img_resized = imutils.resize(img_original, width=200)

# Save the resized image as "resizedImage.png"
cv2.imwrite("dataset/resizedImage.png", img_resized)

# Apply Gaussian blur to the image
img_blurred = cv2.GaussianBlur(img_original, (21, 21), 0)

# Save the blurred image as "gaussianImage.png"
cv2.imwrite("dataset/gaussianImage.png", img_blurred)

# Apply thresholding to the b/w image
img_thresholded = cv2.threshold(img_gray, 180, 255, cv2.THRESH_BINARY)[1]

# Save the thresholded image as "thresholdImage.png"
cv2.imwrite("dataset/thresholdImage.png", img_thresholded)

# Display the images
# cv2.imshow("Original", img_original)
# cv2.imshow("Grayscale", img_gray)
# cv2.imshow("Resized", img_resized)
# cv2.imshow("Blurred", img_blurred)
# cv2.imshow("Thresholded", img_thresholded)

# Open the default camera
try:
    cam = cv2.VideoCapture(0)
except Exception as e:
    print(f"Error: Failed to open camera: {e}")
    exit()

# Loop over the frames from the camera
while True:
    # Capture a frame from the camera
    ret, frame = cam.read()

    # Check if the frame was successfully captured
    if not ret:
        print("Error: Failed to capture frame from camera")
        break

    # Display the frame in a window called "camera"
    cv2.imshow("Camera", frame)

    # Wait for a key press and check if the "q" key was pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Release the camera and close all windows
cam.release()
cv2.destroyAllWindows()
cv2.waitKey(1) # ensure that all windows are closed