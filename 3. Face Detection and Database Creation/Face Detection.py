import cv2

# Load the classifier
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Start the camera
cam = cv2.VideoCapture(0)

while True:
    # Capture a frame
    ret, frame = cam.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = cascade.detectMultiScale(gray, 1.3, 4)

    # Draw a rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('Face Detection', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera
cam.release()

# Close all windows
cv2.destroyAllWindows()
