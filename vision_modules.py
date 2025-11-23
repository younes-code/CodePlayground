import cv2
import numpy as np

def track_color(lower_color, upper_color, min_size=300, max_size=3000):
    """
    Tracks objects of a specific color in the video stream.

    Parameters:
    - lower_color: Lower HSV boundary for the target color.
    - upper_color: Upper HSV boundary for the target color.
    - min_size: Minimum contour area to consider.
    - max_size: Maximum contour area to consider.
    """
    # Open the laptop's camera
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Unable to access the camera.")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to read frame.")
            break

        # Convert the frame to HSV color space
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create a mask for the specified color
        mask = cv2.inRange(hsv_frame, lower_color, upper_color)

        # Find contours of the detected color
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            # Filter contours by size
            contour_area = cv2.contourArea(contour)
            if min_size < contour_area < max_size:
                # Get the bounding box
                x, y, w, h = cv2.boundingRect(contour)
                # Draw a rectangle around the object
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Show the frame with the bounding box
        cv2.imshow("Tracking", frame)

        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Define HSV ranges for different colors
    # Uncomment the color you want to track

    # Red color range
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])

    # Green color range
    # lower_green = np.array([40, 50, 50])
    # upper_green = np.array([80, 255, 255])

    # Blue color range
    # lower_blue = np.array([100, 150, 0])
    # upper_blue = np.array([140, 255, 255])

    # Yellow color range
    # lower_yellow = np.array([20, 100, 100])
    # upper_yellow = np.array([30, 255, 255])

    # Orange color range
    # lower_orange = np.array([10, 100, 20])
    # upper_orange = np.array([25, 255, 255])

    # Purple color range
    # lower_purple = np.array([130, 50, 50])
    # upper_purple = np.array([160, 255, 255])

    # Example usage: Tracking red with size constraints
    track_color(lower_red, upper_red, min_size=300, max_size=2000)
