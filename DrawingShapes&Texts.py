import cv2
import numpy as np

image = np.zeros((512, 512, 3), np.uint8)
# 0 to 255 is the base value of the color(B, G, R)
print(image)

#To change the colors
# image[:] = 255, 0, 0

#To Draw a Line
cv2.line(image, (0, 0), (image.shape[1], image.shape[0]), (0,255,0), 2) #-> The pt1 denotes where to start. In pt2 we have to input width and height.

#To Draw a Rectangle
cv2.rectangle(image, (250, 50), (450, 150), (0, 0, 255), cv2.FILLED) #-> cv2.FILLED is used to fill the given color inside the shape.

#To Draw a Circle
cv2.circle(image, (150, 350), 100, (255, 0, 0), cv2.FILLED)

#To Write a Text
cv2.putText(image, "Sushyam Sai", (50, 45), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=2, color=(100, 212, 150))


cv2.imshow("Image", image)


cv2.waitKey(0)
