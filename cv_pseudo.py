import cv2
import numpy as np

img = cv2.imread("006.jpg")

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(grey,127,255,1)

cv2.imshow('img',thresh)
cv2.waitKey(0)

contours, h = cv2.findContours(thresh, 1, cv2.CHAIN_APPROX_SIMPLE)
contours.sort(key = len)
for contour in contours:

    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)

    #star - > yellow
    if len(approx) == 10:
        cv2.drawContours(img, [contour],0, (0,255,255), -1)

    #circle -> black
    elif len(approx) >= 11:
        cv2.drawContours(img, [contour], 0, (0,0,0), -1)

    #triangle -> green
    elif len(approx) == 3:
        cv2.drawContours(img,[contour],0,(0,255,0),-1)

    #square -> blue
    elif len(approx) == 4:
        cv2.drawContours(img, [contour],0, (255,0,0),-1)

    #pentagon -> red
    elif len(approx) == 5:
        cv2.drawContours(img, [contour],0, (0,0,255), -1)