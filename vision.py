import cv2
import numpy as np

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Set the window to full screen
cv2.namedWindow('Frame', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('Frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Set the resolution of the webcam capture
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 448)

# Set the frame rate to 50 Hz
cap.set(cv2.CAP_PROP_FPS, 50)


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Flip the frame horizontally (mirror effect)
    frame = cv2.flip(frame, 1)

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define the range for the red color in HSV
    lower_red = np.array([0, 150, 70])
    upper_red = np.array([10, 255, 255])
    
    # Create a mask for the red color
    mask = cv2.inRange(hsv, lower_red, upper_red)
    
    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # If any contours are found
    if contours:
        c = max(contours, key=cv2.contourArea)
        # Get the bounding box coordinates
        x, y, w, h = cv2.boundingRect(c)
        # Check if the blob size is above a certain threshold
        if cv2.contourArea(c) > 200:  # Adjust the threshold value as needed
            # Draw a rectangle around the largest contour
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Display the resulting frame
    cv2.imshow('Frame', frame)
    
    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()