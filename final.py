import cv2
import imutils
import numpy as np

image = cv2.imread("map.png")
finalImage = np.zeros_like(image)

finalColorG = 100

blue = 0
green = 0
red = 0

blueMax = 0
greenMax = 0
redMax = 0

for i in range(1, 51):

    if i % 3 == 1:
        redMax += 15
        red = redMax
        green = 0
        blue = 0
    
    if i % 3 == 2:
        greenMax += 15
        green = greenMax
        red = 0
        blue = 0
    
    if i % 3 == 0:
        blueMax += 15
        blue = blueMax
        red = 0
        green = 0
    
    lowerBGR = np.array([blue, green, red])
    upperBGR = np.array([blue , green, red])
    mask = cv2.inRange(image, lowerBGR, upperBGR)

    edgedMask = cv2.Canny(mask, 30, 150)
    edgedMask = cv2.morphologyEx(edgedMask, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
    contoursMask = cv2.findContours(edgedMask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contoursMask = imutils.grab_contours(contoursMask)

    filled = cv2.cvtColor(edgedMask, cv2.COLOR_GRAY2BGR)
    filled = cv2.fillPoly(filled, pts = contoursMask, color = (0, finalColorG, 0))
    finalImage = finalImage + filled
    finalColorG += 2

finalImage = cv2.resize(finalImage, None, fx = 0.75, fy = 0.75)
cv2.imshow("Final", finalImage)
cv2.waitKey(0)
cv2.destroyAllWindows()