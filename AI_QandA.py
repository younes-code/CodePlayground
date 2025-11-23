import cv2
import numpy as np
import pygame
import random

# Initialize pygame for font rendering
pygame.font.init()

# Set up display for the game
screen_width = 800
screen_height = 600
screen = np.zeros((screen_height, screen_width, 3), dtype=np.uint8)  # Create a black screen for OpenCV

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Define font for text rendering
font = cv2.FONT_HERSHEY_SIMPLEX

# Questions and answers (sequential, not random)
questions = [
    {"question": "What is 2 + 2?", "answers": ["3", "4"], "correct": "4"},
    {"question": "What is the capital of France?", "answers": ["Paris", "London"], "correct": "Paris"},
    {"question": "What is the largest planet?", "answers": ["Jupiter", "Earth"], "correct": "Jupiter"},
]

# Function to render text on the screen
def display_text(image, text, color, x, y, font_size=1, thickness=2):
    cv2.putText(image, text, (x, y), font, font_size, color, thickness)

# Function to track the color object and simulate mouse cursor movement
def track_color(lower_color, upper_color, min_size=300, max_size=3000):
    # Start video capture
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Unable to access the camera.")
        return

    score = 0
    game_running = True
    question_index = 0  # Start from the first question
    cursor_x, cursor_y = screen_width // 2, screen_height // 2  # Initial cursor position
    answered = False  # Flag to check if a question has been answered

    while game_running:
        # Capture the frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to read frame.")
            break

        # Convert the frame to HSV color space for color tracking
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create a mask based on the color
        mask = cv2.inRange(hsv_frame, lower_color, upper_color)

        # Find contours of the color objects
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Track the largest detected object
        largest_contour = None
        max_area = 0
        for contour in contours:
            contour_area = cv2.contourArea(contour)
            if min_size < contour_area < max_size and contour_area > max_area:
                max_area = contour_area
                largest_contour = contour

        if largest_contour is not None:
            # Find the bounding box of the detected color object
            x, y, w, h = cv2.boundingRect(largest_contour)
            cursor_x, cursor_y = x + w // 2, y + h // 2  # Set cursor to center of the object

        # Overlay the game interface and video on the same screen
        # Display the video stream as the background
        frame_resized = cv2.resize(frame, (screen_width, screen_height))

        # Get the current question
        if question_index < len(questions):
            question = questions[question_index]
            question_text = question["question"]
            correct_answer = question["correct"]
            random.shuffle(question["answers"])
            answer_1 = question["answers"][0]
            answer_2 = question["answers"][1]

            # Answer positions
            answer_1_pos = (100, 300)
            answer_2_pos = (100, 400)

            # Draw the question and answers over the video stream
            display_text(frame_resized, question_text, BLACK, 100, 100)
            display_text(frame_resized, answer_1, GREEN if answer_1 == correct_answer else RED, *answer_1_pos, font_size=0.8)
            display_text(frame_resized, answer_2, GREEN if answer_2 == correct_answer else RED, *answer_2_pos, font_size=0.8)

            # Draw a box around the answers
            cv2.rectangle(frame_resized, (answer_1_pos[0], answer_1_pos[1]), (answer_1_pos[0] + 200, answer_1_pos[1] + 50), BLACK, 2)
            cv2.rectangle(frame_resized, (answer_2_pos[0], answer_2_pos[1]), (answer_2_pos[0] + 200, answer_2_pos[1] + 50), BLACK, 2)

            # Check if the tracked object is over an answer box
            if answer_1_pos[0] <= cursor_x <= answer_1_pos[0] + 200 and answer_1_pos[1] <= cursor_y <= answer_1_pos[1] + 50:
                if answer_1 == correct_answer and not answered:
                    score += 1
                    answered = True
            elif answer_2_pos[0] <= cursor_x <= answer_2_pos[0] + 200 and answer_2_pos[1] <= cursor_y <= answer_2_pos[1] + 50:
                if answer_2 == correct_answer and not answered:
                    score += 1
                    answered = True

            # If the question has been answered, move to the next question after a short delay
            if answered:
                cv2.putText(frame_resized, "Next Question...", (250, 500), font, 1, BLACK, 2)
                pygame.time.wait(1000)  # Wait for 1 second before showing next question
                answered = False
                question_index += 1  # Move to next question

        # Draw the "cursor" (tracked object)
        cv2.rectangle(frame_resized, (cursor_x - 10, cursor_y - 10), (cursor_x + 10, cursor_y + 10), GREEN, 2)

        # Display the score
        display_text(frame_resized, f"Score: {score}", BLACK, 300, 500, font_size=0.8)

        # Show the frame with video and game interface in the same window
        cv2.imshow("Game with Object Tracking", frame_resized)

        # Handle quitting the game with 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            game_running = False

    cap.release()
    cv2.destroyAllWindows()

# Define HSV ranges for different colors (uncomment the one you want to use)
# Red color range
# lower_red = np.array([0, 120, 70])
# upper_red = np.array([10, 255, 255])

# Green color range (uncomment to track green)
lower_green = np.array([40, 50, 50])
upper_green = np.array([80, 255, 255])

# Run the game with tracking
if __name__ == "__main__":
    track_color(lower_green, upper_green, min_size=300, max_size=2000)  # Track red color
