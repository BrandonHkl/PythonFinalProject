import cv2
import imutils
import numpy as np

image = cv2.imread("map.png")
cv2.imshow("Map", image)
cv2.waitKey(0)

blurred = cv2.blur(image, (3, 3))
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)

gray_scaled = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayed", gray_scaled)
cv2.waitKey(0)

edged = cv2.Canny(gray_scaled, 30,150)
cv2.imshow("Edge Detection", edged)
cv2.waitKey(0)

contours = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
text = "There are {} objects here.".format(len(contours))
cv2.putText(edged, text, (10,25), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(240, 0, 159), 2)
cv2.imshow("Description", edged)
cv2.waitKey(0)

cv2.destroyAllWindows()

lowerBGR = np.array([101, 18, 174])
upperBGR = np.array([131, 48, 204])
mask = cv2.inRange(image, lowerBGR, upperBGR)
cv2.imshow("Mask", mask)
cv2.waitKey(0)

edgedMask = cv2.Canny(mask, 30, 150)
cv2.imshow("Edge Detection", edgedMask)
cv2.waitKey(0)

contoursMask = cv2.findContours(edgedMask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contoursMask = imutils.grab_contours(contoursMask)

filled = cv2.fillPoly(edgedMask, pts = contoursMask, color=(125, 93, 67))
filled = cv2.cvtColor(filled, cv2.COLOR_GRAY2RGB)
cv2.imshow("Filled", np.array(image) + filled)
cv2.waitKey(0)

cv2.destroyAllWindows()