import cv2
import numpy as np

frameWidth = 1000
frameHeight = 800

cap = cv2.VideoCapture(0) #--> If we enter "0" we can turn on the default webcam
cap.set(3, frameWidth)
cap.set(4, frameHeight)

def empty(a):
    pass

# Create a Track Bar for HUE, Saturation and Value
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 400, 230)
cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)
cv2.createTrackbar("HUE Max", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)
cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)
cv2.createTrackbar("VALUE Min", "HSV", 0, 255, empty)
cv2.createTrackbar("VALUE Max", "HSV", 255, 255, empty)

while True:
    sucess,image = cap.read()

    imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) #-> Converting a BGR image to HSV

    hue_min = cv2.getTrackbarPos("HUE Min", "HSV")
    hue_max = cv2.getTrackbarPos("HUE Max", "HSV")
    sat_min = cv2.getTrackbarPos("SAT Min", "HSV")
    sat_max = cv2.getTrackbarPos("SAT Max", "HSV")
    value_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    value_max = cv2.getTrackbarPos("VALUE Max", "HSV")


#-> Creating Masking
    lower = np.array([hue_min, sat_min, value_min])
    upper = np.array([hue_max, sat_max, value_max])

    mask = cv2.inRange(imageHSV, lower, upper)

    result = cv2.bitwise_and(image, image, mask=mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    hStack = np.hstack([image, mask, result])

    # cv2.imshow("Original", image)
    # cv2.imshow("HSV Format", imageHSV)
    # cv2.imshow("Mask Image", mask)
    # cv2.imshow("Result", result)
    cv2.imshow("Horizontal Stack", hStack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release() #-> Always call cap.release() at the end of your code that reads frames from a video to prevent potential resource leaks
cv2.destroyAllWindows()
