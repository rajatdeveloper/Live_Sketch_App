"""Project - Computer Vision that creates live sketch.
   Rajat Singhal : singhal.rajat97@gmail.com
   B.Tech 4th Semester, Computer Science & Engineering"""

import numpy as np
import cv2
#sketch generating function
def sketch(image):
    #convert image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #clean up image using Gaussian Blur
    img_gray_blur =cv2.GaussianBlur(img_gray,(5,5),0)

    #Extract Edges
    canny_edges = cv2.Canny(img_gray_blur,10,70)

    #Do an invert binarize the image
    ret, mask = cv2.threshold(canny_edges,70,255,cv2.THRESH_BINARY_INV)

    return mask

#Initialize webcam, cap is the object provided by VideoCapture
#It contains a boolean indicating if it was sucessful (ret)
#It also contains the image collected from webcam (frame)
cap =cv2.VideoCapture(0)

while True:
    ret, frame =cap.read()
    cv2.imshow('Our Live Sketcher',sketch(frame))
    if cv2.waitKey(1)==13 :#13 is the Enter waitKey
        break

#Release camera and close windows
cap.release()
cv2.destroyAllWindows()
