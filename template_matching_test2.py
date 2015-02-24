import numpy as np
import cv2

result = cv2.matchTemplate(img,template,cv.CV_TM_SQDIFF)

#the get the best match fast use this:
(min_x,max_y,minloc,maxloc) = cv2.minMaxLoc(result)
(x,y) = minloc

#get all the matches:
result2 = np.reshape(result, result.shape[0]*result.shape[1])
sort = np.argsort(result2)
(y1, x1) = np.unravel_index(sort[0], result.shape) #best match
(y2, x2) = np.unravel_index(sort[1], result.shape) #second best match