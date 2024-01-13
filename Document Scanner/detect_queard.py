import cv2
import numpy as np
import os

root = os.getcwd()
print(root)
imgPath = os.path.join(root, '/chess.png')
img = cv2.imread(imgPath)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray, maxCorners=4, qualityLevel=0.01, minDistance=10)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 3, 255, 1)


cv2.imshow('corners', img)
cv2.waitKey(0)
cv2.destroyAllWindows()