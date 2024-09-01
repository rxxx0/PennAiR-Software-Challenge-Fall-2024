import cv2
import numpy as np

def trace(img_path):
    
    # reads the image
    img = cv2.imread(img_path)

    # Canny edge detection
    edges = cv2.Canny(img, 0, 0)

    # due to the "grainy" nature of the grass, many of the dark spots are incorrectly detected as edges.
    # we can get around this by dilating the Canny output, as this will "close" the small false edges 
    # without destroying the big shape edges that we are seeking to isolate.
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,4))
    edges = cv2.morphologyEx(edges, cv2.MORPH_DILATE, kernel)

    # since we heavily dilated our edges, we now have a white image with negatives of the shapes.
    # we want the opposite of this, so we simply invert our image.
    edges = cv2.bitwise_not(edges)

    # finds the contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # makes a copy of the original image so we can trace the shapes on it
    overlay = img.copy()

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
