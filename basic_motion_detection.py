import cv2
import numpy as np

# Open the default camera (index 0) for video capture
cap = cv2.VideoCapture(0)

# Read the initial frames from the camera feed
ret, frame1 = cap.read()
ret, frame2 = cap.read()

# Main loop for motion detection
while cap.isOpened():
    # Calculate the absolute difference between two consecutive frames
    diff = cv2.absdiff(frame1, frame2)

    # Convert the difference frame to grayscale
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to the grayscale image
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply binary thresholding to create a binary motion mask
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    # Dilate the thresholded image to fill gaps and enhance motion regions
    dilated = cv2.dilate(thresh, None, iterations=3)

    # Find contours in the dilated image
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through each detected contour
    for contour in contours:
        # Get the bounding rectangle around the contour
        (x, y, w, h) = cv2.boundingRect(contour)

        # If the contour area is too small, skip it as noise
        if cv2.contourArea(contour) < 900:
            continue

        # Draw a green rectangle around the region of detected motion
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Add a "Movement" label near the rectangle
        cv2.putText(frame1, "status:{}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    # Display the processed frame with motion detection
    cv2.imshow("feed", frame1)

    # Update frame1 with the content of frame2 for the next iteration
    frame1 = frame2

    # Read the next frame from the camera feed
    ret, frame2 = cap.read()

    # Break the loop if the 'Esc' key (key code 27) is pressed
    if cv2.waitKey(40) == 27:
        break

# Release resources and close OpenCV windows
cv2.destroyAllWindows()
cap.release()
