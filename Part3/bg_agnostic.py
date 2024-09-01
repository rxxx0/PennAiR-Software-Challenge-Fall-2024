import cv2
import numpy as np

def trace(frame):

    # converts the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # denoises the frame
    denoised = cv2.bilateralFilter(gray, 4, 10, 20)

    # adaptive thresholding (we can't directly apply Canny like we did in part 1 and 2 since the shapes are not of uniform color)
    thresh = cv2.adaptiveThreshold(denoised, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 9, 2)

    # closes the small extraneous edges that remain after thresholding
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (12, 12))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

    # Canny edge detection
    edges = cv2.Canny(closed, 0, 0)

    # finds the contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # makes a copy of the original frame so we can trace the shapes on it
    overlay = frame.copy()

    for contour in contours:
        # draws the contour
        cv2.drawContours(overlay, [contour], -1, (0, 0, 0), 2)

        # calculates and marks the center
        moments = cv2.moments(contour)
        if moments['m00'] != 0:
            # recall from physics that the centroid of a shape (x, y) is given by (moment about x / Area, moment about y / Area)
            cX = int(moments['m10'] / moments['m00'])
            cY = int(moments['m01'] / moments['m00'])
            cv2.circle(overlay, (cX, cY), 4, (0, 0, 255), -1)  # places red dot on the center
            cv2.putText(overlay, f'({cX}, {cY})', (cX - 48, cY + 68), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 0, 0), 2) # writes the coordinates of the center

    return overlay

def makeVideo(video_path, output_path):

    # opens the video
    cap = cv2.VideoCapture(video_path)

    # gets video properties and initializes the output
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # traces the current frame
        traced_frame = trace(frame)

        # appends the frame to the output video
        out.write(traced_frame)

    # releases resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()
